MOD = 10 ** 9 + 7
N = int(input())
all = 10**N
a = 9**N
b = 9**N
ab = 8**N
ans = all-(a+b)+ab
print(ans%MOD)