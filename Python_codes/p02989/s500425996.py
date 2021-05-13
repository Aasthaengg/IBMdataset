_ = input()
D = [int(i) for i in input().split()]

D.sort()
l = len(D)
lower = D[(l // 2) - 1]
upper = D[(l // 2)]

print(upper - lower)