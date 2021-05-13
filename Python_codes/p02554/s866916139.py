'''
参考
https://qiita.com/u2dayo/items/98917c94c89c77b9b3a1#c%E5%95%8F%E9%A1%8Cubiquity
'''

MOD = 10 ** 9 + 7

N = int(input())

ans = pow(10, N)
ans -= 2 * pow(9, N)
ans += pow(8, N)
ans %= MOD

print(ans)
