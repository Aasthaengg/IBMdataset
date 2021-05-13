k, a, b = map(int, input().split())
if b-1 <= a:
    print(1 + k)
else:
    k -= a-1
    cnt = a
    if k%2 == 1:
        cnt += 1
        k -= 1
    cnt += (b-a) * k//2
    print(cnt)
