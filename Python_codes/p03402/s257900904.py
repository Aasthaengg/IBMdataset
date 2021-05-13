a, b = map(int, input().split())
g = [['.']*100 for _ in range(100)]
for j in range(100):
    for i in range(50,100):
        g[i][j] = '#'
#print_dp(g)

b_cnt = 1
i = 0
j = 0
while b_cnt < b:
    g[i][j] = '#'
    j += 2
    if j >= 100:
        i += 2
        j = 0
    b_cnt += 1
a_cnt = 1
i = 99
j = 0
while a_cnt < a:
    g[i][j] = '.'
    j += 2
    if j >= 100:
        i -= 2
        j = 0
    a_cnt += 1
print("100 100")
for i in range(100):
    print("".join(g[i]))