N = int(input())
A = list(map(int, input().split()))

total = sum(A)

diff = total
ans = -1
for index, a in enumerate(A):
    if diff > abs(total - N * a):
        ans = index
        diff = abs(total - N * a)

print (ans)
