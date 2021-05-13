a,b,c = map(int,input().split())
k = int(input())
d = 0
for i in range(k+1):
    if b <= a:
        b *= 2
    elif c <= b:
        c *= 2
    else:
        d = 1
if d == 0:
    print("No")
else:
    print("Yes")