N = int(input())
lr = [list(map(int,(input().split()))) for _ in range(N)]
ans = []
for i in range(N):
    ans.append(lr[i][1]-lr[i][0]+1)
print(sum(ans))