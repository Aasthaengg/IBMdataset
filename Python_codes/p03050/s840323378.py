#--約数のリスト--#

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            upper_divisors.append(n//i)
        i += 1
    return lower_divisors,upper_divisors

#--処理の開始--#
N = int(input())
l,u = make_divisors(N)
ans = 0
for ln,un in zip(l,u):
    if un-1>ln:
        ans += un-1
print(ans)
    

