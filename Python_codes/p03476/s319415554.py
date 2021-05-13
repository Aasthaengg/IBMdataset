import math
def is_prime(n):
    if n == 1: return False
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True
Q = int(input())
cnt = [0]*(10**5+1)
for i in range(1,10**5+1):
    if i % 2 == 0:
        cnt[i] = cnt[i-1]
        continue
    if is_prime(i) and is_prime((i+1)//2):
        cnt[i] = cnt[i-1] + 1
    else:
        cnt[i] = cnt[i-1]
for _ in range(Q):
    l, r = map(int, input().split())
    print(cnt[r]-cnt[l-1])