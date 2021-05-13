k = int(input())
a = list(map(int, input().split()))

max_ans = 2
for i in range(k)[::-1]:
    max_ans = (max_ans // a[i]) * a[i] + (a[i] - 1)
    
min_ans = 2
for i in range(k)[::-1]:
    min_ans = -((-min_ans) // a[i]) * a[i]

tmp = max_ans
for i in range(k):
    tmp = (tmp // a[i]) * a[i]
if tmp != 2:
    print(-1)
    exit()
    
tmp = min_ans
for i in range(k):
    tmp = (tmp // a[i]) * a[i]
if tmp != 2:
    print(-1)
    exit()

print(min_ans, max_ans)