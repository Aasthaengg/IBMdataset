k, a, b = map(int, input().split())

if b <= a+1 or k <= a:
    print(k+1)
    exit(0)

cnt = 1
k -= a-1
cnt += a-1
cnt += (k // 2) * (b-a)
cnt += k % 2
print(cnt)