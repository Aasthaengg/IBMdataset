n = int(input())
a = list(map(int, input().split()))[::-1]

min_ans = 2
max_ans = 2

for i in range(n):
    min_ans = -((-min_ans) // a[i]) * a[i]
    
for i in range(n):
    max_ans = (max_ans// a[i]) * a[i] +a[i] - 1

a = a[::-1]
tmp_ans = min_ans
tmp_ans2 = max_ans
for i in range(n):
    tmp_ans = (tmp_ans // a[i]) * a[i]
    tmp_ans2 = (tmp_ans // a[i]) * a[i]
    
if tmp_ans == 2 and tmp_ans2 == 2:
    print(min_ans, max_ans)
else:
    print(-1)