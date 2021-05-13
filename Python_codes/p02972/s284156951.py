n = int(input())
a = [0] + list(map(int,input().split()))
b = [0]*(n+1)
ans = 1
for i in range(1,n+1):
    b[-i] = sum(a[::n+1-i])
    if b[-i]%2 != a[-i]:
        if a[-i] == 0:
            a[-i] = 1
        else:
            a[-i] = 0
if ans == -1:
    print(-1)
else:
    lis = []
    for i in range(1,n+1):
        if a[i] == 1:
            lis.append(str(i))
    print(len(lis))
    print(" ".join(lis))