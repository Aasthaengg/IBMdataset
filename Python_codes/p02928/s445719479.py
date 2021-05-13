n,k = list(map(int, input().split()))
a = list(map(int, input().split()))

# 数列の自分より後方で自分より小さい数
c1 = sum([1 if a[i]>j else 0 for i in range(n) for j in a[i+1:]])

# 数列内で自分より小さい数
from collections import Counter
ca = Counter(a)

c2 = 0
for n1,cnt1 in ca.items():
    for n2,cnt2 in ca.items():
        if n2<n1:
            c2+=cnt2*cnt1

MOD=10**9+7
k %= MOD
ans = (c1*k)%MOD + (c2*k*(k-1)//2)%MOD
ans %= MOD
print(ans)
