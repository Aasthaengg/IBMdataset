s = int(input())

if s % 10**9 == 0:
    y2 = s // 10**9
else:
    y2 = s // 10**9 + 1
    
y1 = 10**9*y2 - s

print(0,0,10**9,y1,1,y2)