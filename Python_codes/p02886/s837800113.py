N = int(input())
D = [int(s) for s in input().split(' ')]
D_sum = sum(D)
ret = 0
for d in D:
    ret += d * (D_sum - d)

print(ret // 2)

