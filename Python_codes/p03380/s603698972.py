n = int(input())
a = [int(x) for x in input().split()]

base = max(a)
tmp = 10**9
tmp_i = 0
for x in a:
    if x == base:
        pass
    elif abs(base - 2*x) < tmp:
        tmp = abs(base - 2*x)
        tmp_i = x

print(base, tmp_i)