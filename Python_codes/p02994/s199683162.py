n, l = map(int, input().split())
li = [l+i for i in range(n)]
INF = 1001001001
mn = INF
sum = 0
for i in li:
    sum += i
    if abs(mn) > abs(i):
        mn = i
print(sum - mn)