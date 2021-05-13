n = int(input())
B = list(map(int, input().split()))

#print(len(B))
ans = []
while B:
    for i in reversed(range(len(B))):
        if B[i] == i+1:
            ans.append(B[i])
            del B[i]
            break
    else:
        print(-1)
        exit()
for i in reversed(range(len(ans))):
    print(ans[i])