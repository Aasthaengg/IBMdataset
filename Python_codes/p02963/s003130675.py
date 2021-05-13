s = int(input())
x = s % 10**9
y = s // 10**9
if x > 0:
    x -= 10**9
    y += 1
print(0,0,10**9,1,-x,y)