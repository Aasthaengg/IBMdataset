N = int(input())
S = input()
m = 10 ** 9 + 7
S_li = list(set(S))
ans = 1
for sl in S_li:
    ans *= S.count(sl) + 1
print((ans - 1) % m)
