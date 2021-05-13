n = int(input())
data = []
for i in range(n):
    a, b = map(int, input().split())
    data.append([a, b, a+b])
a_ans = 0
b_ans = 0
data.sort(key=lambda x: x[2] ,reverse=True)
for i in range(n):
    if i % 2 == 0:
        a_ans += data[i][0]
    else:
        b_ans += data[i][1]
print(a_ans - b_ans)
