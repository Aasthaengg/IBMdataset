n = int(input())
bi = [int(i) for i in input().split()]

ans = []

for i in range(n):
    for j in range(len(bi)):
        if bi[len(bi)-1-j] == len(bi)-1-j+1:
            ans.append(len(bi)-1-j+1)
            del bi[len(bi)-1-j]
            break

if len(ans) != n:
    print(-1)
else:
    for i in range(n):
        print(ans[n-1-i])
