N = int(input())
a = list(map(int, input().split()))
like = []
cnt = 0

for i in range(0, N):
    like.append([i+1, a[i]])

for j, k in like:
    if like[k-1][1] == j:
        cnt += 1

print(cnt // 2)