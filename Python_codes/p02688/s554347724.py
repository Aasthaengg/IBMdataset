n, k = map(int, input().split())
lst = [1]*n

for _ in range(k):
  d = input()
  hv_lst = list(map(int, input().split()))
  for i in hv_lst:
    lst[i-1] = 0
print(lst.count(1))