#  #16586869
n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
now = 1
check = [-1]*(n+1)
for i in range(k):
  if check[now] == -1:
    check[now] = i
    now = a[now]
  else:
    loop = i - check[now] # check?
    afterloop = (k-(i-loop))%loop
    print(check.index((i-loop)+afterloop))
    exit()
print(now)