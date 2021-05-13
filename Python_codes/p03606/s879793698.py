# coding: utf-8

n = int(input().rstrip())

ans = [k[1] - k[0] + 1 for k in[[int(i) for i in input().rstrip().split(" ")] for j in range(n)]]
print(sum(ans))