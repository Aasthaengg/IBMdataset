N = int(input())
X = list(map(int, input().split()))
nx = [X[i] for i in range(N)]
nx.sort()
ans2 = (nx[N//2])
ans3 = (nx[N//2-1])

for i in range(N):
    if X[i] <= nx[N//2-1]:
        print(ans2)
    elif X[i] >= nx[N//2]:
        print(ans3)

