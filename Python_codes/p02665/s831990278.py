n = int(input())
a = list(map(int, input().split()))

ans = 0

if a[0] > 0:
    if n == 0 and a[0] == 1:
        print(1)
        exit()
    else:
        print(-1)
        exit()

# node_list_1 は深いところから見たNode数の最大値
# node_list_2 は根から見たNode数の最大値
node_list_1 = [0] * (n + 1)
node_list_2 = [0] * (n + 1)

node_list_1[n] = a[n]
node_list_2[0] = 1

for i in range(n-1, -1, -1):
    node_list_1[i] = node_list_1[i+1] + a[i]

for j in range(1, n+1):
    node_list_2[j] = (node_list_2[j-1] - a[j-1]) * 2
    if node_list_2[j] < a[j]:
        print(-1)
        exit()

for k in range(n+1):
    ans += min(node_list_1[k], node_list_2[k])

print(ans)
