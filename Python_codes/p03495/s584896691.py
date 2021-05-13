N, K = map(int, input().split())
A = list(map(int, input().split()))
li = [0]*10**6
for i in range(N):
    li[A[i]] += 1
# print(li)
li.sort(reverse=True)
# print(li)
print(sum(li[K:]))