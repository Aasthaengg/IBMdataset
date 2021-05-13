n = int(input())
x = list(map(int, input().split()))
num = 10**10
for p in range(100):
    cnt = 0
    for i in range(n):
        cnt += (x[i] - p)**2
    num = min(num, cnt)
print(num)