inf = 10 ** 20
n, m = map(int, input().split())
a_list = []
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    a_list.append([a, b, c])
a_list[0][0] = 0
d = [-inf for _ in range(n)]
d[0] = 0
for i in range(m):
    a, b, c = a_list[i]
    d[b] = max(d[a] + c, d[b])
temp = d[-1]
for i in range(m):
    a, b, c = a_list[i]
    d[b] = max(d[a] + c, d[b])
if temp != d[-1]:
    print("inf")
else:
    print(d[-1])