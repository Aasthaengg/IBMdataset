n = int(input())

"""
a x b = n-c
となる組合せを探す。
c>=1なので、a x b <= n-1ならばcを適当に決めて
組合せにできる
"""
n-=1
ans = 0
a = 1
while a <= n:
    ans += n//a
    a+=1
print(ans)
