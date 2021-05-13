n = int(input())
a,b = map(int,input().split())
l = list(map(int,input().split()))
c = [0,0,0]
for i in l:
    if i <= a:
        c[0] += 1
    elif i > b:
        c[2] += 1
    else:
        c[1] += 1
print(min(c))