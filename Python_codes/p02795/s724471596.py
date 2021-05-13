ans = 100
H = int(input())
W = int(input())
N = int(input())

for i in range(H+1):
    for j in range(W+1):
        if i * W + j * H - i * j >= N:
            ans = min(ans, i+j)

print(ans)