n, k = map(int, input().split())
lst = list(map(int, input().split()))
idx = lst.index(1)
k -= 1
a = (len(lst[:idx]) + k - 1) // k
b = (len(lst[idx + 1:]) + k - 1) // k
c = ((n - 1) + k - 1) // k
print(min(c, a + b))