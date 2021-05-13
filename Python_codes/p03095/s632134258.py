n = int(input())
a = list(input())
b = list(set(a))
ans = 1
for i in b:
    ans %= 10**9+7
    ans *= a.count(i)+1
print((ans-1)%(10**9+7))