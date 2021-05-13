N,K = map(int, input().split())
H = list(map(int, input().split()))
steps = [0]*N
steps[1] = abs(H[0]-H[1])
for i in range(2,N):
    steps[i] = min([steps[j] + abs(H[j]-H[i]) for j in range(max(0,i-K),i)])
print(steps[-1])