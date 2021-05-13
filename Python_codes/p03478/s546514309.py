n, a, b = map(int, input().split())
sum = 0

for i in range(1,n+1):
    L = len(str(i))
    cnt = 0
    for j in range(L):
        cnt += int(str(i)[j])
    if a <= cnt <= b:
        sum += i

print(sum)