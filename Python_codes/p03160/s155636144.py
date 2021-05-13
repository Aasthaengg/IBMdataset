N = int(input())
h = list(map(int, input().split()))

opt = [0] * len(h)
opt[1] = abs(h[0]-h[1])

for i in range(2,len(h)):
    A = opt[i-1] + abs(h[i-1] - h[i])
    B = opt[i-2] + abs(h[i-2] - h[i])
    opt[i] = min(A, B)
print(opt[-1])