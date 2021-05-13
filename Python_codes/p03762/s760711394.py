n, m = [int(i) for i in input().split(' ')]
x_list = [int(i) for i in input().split(' ')]
y_list = [int(i) for i in input().split(' ')]

x_res = 0
for i in range(n):
    x_res += (i-(n-i-1))*x_list[i]
y_res = 0
for j in range(m):
    y_res += (j-(m-j-1))*y_list[j]
print((x_res*y_res) % (10**9+7))