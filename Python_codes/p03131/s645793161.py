K, A, B = map(int, input().split())

if B-A <= 2:
    print(K+1)
    exit(0)

if 1+(K-2) < A:
    print(K+1)
    exit(0)

exchange_times, last = divmod(K-(A-1), 2)
profit = B - A
ans = A + exchange_times * profit + last
print(ans)
