K = int(input())
N = 50
num = [i for i in range(N)]
for i in range(N):
    num[i] += K//N
r = K%N
for i in range(r):
    num[i] += N
    for j in range(N):
        if j != i:
            num[j] -= 1
print(N)
print(*num)
