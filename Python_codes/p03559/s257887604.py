n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))

a_list.sort()
b_list.sort()
c_list.sort()
n_b = []
current = 0
for i in range(n):
    a = a_list[i]
    while current <= n-1 and b_list[current] <= a:
        current += 1
    n_b.append(n-current)
n_c = []
current = 0
for i in range(n):
    b = b_list[i]
    while current <= n-1 and c_list[current] <= b:
        current += 1
    n_c.append(n-current)
cum_nc = [0]*n
cum_nc[0] = n_c[n-1]
for i in range(1, n):
    cum_nc[i] = cum_nc[i-1] + n_c[n-1-i]
ans = 0

for i in n_b:
    if i > 0:
        ans += cum_nc[i-1]
print(ans)
