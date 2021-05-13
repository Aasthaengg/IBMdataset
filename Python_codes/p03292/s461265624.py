a1, a2, a3 = map(int, input().split())
aa = sorted([abs(a1-a2), abs(a2-a3), abs(a3-a1)])
print(sum(aa[:2]))