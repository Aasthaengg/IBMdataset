n = int(input())
a = [int(x) for x in input().split()]

sum_a = sum(a)
tmp = 0
p = sum_a - 2 * tmp

for x in a:
    tmp += x
    p = min(p, abs(sum_a - 2 * tmp))

print(p)