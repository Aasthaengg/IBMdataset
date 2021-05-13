from math import gcd
from collections import defaultdict

N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
MOD = 10**9 + 7

d = defaultdict(int)#defaultdictで数えあげ
cnt_00 = 0
cnt_0b = 0
cnt_a0 = 0
for a,b in AB:
    if a == b == 0:
        cnt_00 += 1
    elif a == 0:
        cnt_a0 += 1
    elif b == 0:
        cnt_0b += 1
    else:
        num_gcd = gcd(a,b)
        grad = 1 if a * b > 0 else -1
        a //= num_gcd
        b //= num_gcd
        d[(grad, abs(a), abs(b))] += 1

ans = 1
for k in d.keys():
    if d[k] == 0:
        continue
    
    grad, a, b = k[0], k[1], k[2]
    if (-grad, b, a) in d:
        
        # 傾き a/bのものを一つ以上選ぶ場合（-b/aは選ばない） + -b/aから一つ以上選ぶ場合（a/bは選ばない） + どちらからも選ばない場合
        ans *= (pow(2, d[(grad, a, b)], MOD)-1) + (pow(2, d[(-grad, b, a)], MOD)-1) + 1
        ans %= MOD
        d[(grad, a, b)] = 0
        d[(-grad, b, a)] = 0
    else:
        # a/bから0個以上選ぶ場合
        ans *= pow(2, d[(grad, a, b)], MOD)
        ans %= MOD
        d[(grad, a, b)] = 0

# a,bの一方のみ0の場合 + どちらからも選ばない場合
ans *= (pow(2, cnt_a0, MOD)-1) + (pow(2, cnt_0b, MOD)-1) + 1
ans %= MOD

# 0,0のみを１つだけ入れる場合
ans += cnt_00
# なにも選ばない場合を除く
ans -= 1

ans %= MOD

print(ans)