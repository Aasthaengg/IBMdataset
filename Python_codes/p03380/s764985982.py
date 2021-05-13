n = int(input())
lst = list(map(int, input().split()))

m = max(lst)
r = m//2
k = float('inf')

for i in range(n):
  if lst[i] != m and abs(r-lst[i]) < abs(r-k):
    k = lst[i]
    
print(m, k)