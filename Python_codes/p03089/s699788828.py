n = int(input())
b = list(map(int,input().split()))

ans = []

for i in range(n):
    tmp = -1
    for j,e in enumerate(b):
        if j + 1 == e:
            tmp = max(tmp, e)
    if tmp == -1:
        print(-1)
        exit()
    else:
        ans.append(tmp)
        b = b[:tmp-1] + b[tmp:]

for i in ans[::-1]:
    print(i)
