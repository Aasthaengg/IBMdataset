n = int(input())
s = input()
ans = 1
for x in set(s):
    ans *= s.count(x)+1
print((ans-1)%(10**9+7))
