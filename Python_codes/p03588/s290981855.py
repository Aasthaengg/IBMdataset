N = int(input())
list1 = []
max1 = 0
for i in range(N):
    L = list(map(int, input().split()))
    if max1 < L[0]:
        max1 = L[0]
        ans = sum(L)
print(ans)