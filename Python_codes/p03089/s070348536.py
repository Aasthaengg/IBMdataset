n = int(input())
b = list(map(int,input().split()))
ans = []
for i in range(n):
    r = -1
    for j in range(len(b)):
        if j+1==b[j]:
            r = j
    if r<0:
        ans = [-1]
        break
    ans.append(b.pop(r))
[print(i) for i in ans[::-1]]
