n = int(input())
s1=input()
s2=input()
mod = 10**9+7

if s1[0]==s2[0]: res = 3
else: res = 6

for i in range(1,n):
    if s1[i-1] != s1[i]:
        if s1[i-1] != s2[i-1]:
            if s1[i] != s2[i]: res *= 3
        else: res *= 2

print(res % mod)