from math  import gcd
n, m = map(int, input().split())
s = input()
t = input()

g = gcd(n, m)
ans = n*m//g

"""
最小公倍数の長さで収まらない場合は、何をやってもダメ
"""
for i in range(g):
    if not s[i*n//g] == t[i*m//g]:
        print(-1)
        exit(0)
print(ans)


