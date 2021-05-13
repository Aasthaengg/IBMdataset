n, k = map(int, input().split())
aaa = list(map(int, input().split()))
cnt = 1
b = n - k
while b > 0:
    b -= k - 1
    cnt += 1
print(cnt)