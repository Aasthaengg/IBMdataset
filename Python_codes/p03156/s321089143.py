n = int(input())
a,b = map(int,input().split())
x,y,z = 0,0,0
li = list(map(int,input().split()))
for i in range(n):
    if li[i] <= a:
        x += 1
    elif li[i] >= a + 1 and li[i] <= b:
        y += 1
    else:
        z += 1
print(min(x,y,z))