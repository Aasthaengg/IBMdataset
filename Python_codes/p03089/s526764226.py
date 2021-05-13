n = int(input())
p = list(map(int,input().split()))
ans = []
for i in range(n):
    fla = 0
    for j in reversed(range(n-i)):
        if p[j] == j+1:
            ans.append(p.pop(j))
            fla = 1
            break
    if fla == 0:
        print(-1)
        exit()

for i in reversed(range(n)):
    print(ans[i])