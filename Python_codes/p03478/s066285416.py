n, a, b = map(int, input().split())
cnt = 0
for i in range(1,n+1) :
    num = list(str(i))
    num = map(int, num)
    if a <= sum(num) <= b :
        cnt += i
print(cnt)
