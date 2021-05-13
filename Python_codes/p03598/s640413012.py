N = int(input())
K = int(input())
x = list(map(int, input().split()))

l = 0
for i in range(N):
    if (x[i] <= K/2):
        l += 2 * x[i]
    else:
        l += 2 *(K-x[i])

print(l)



