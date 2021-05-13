N = int(input())
d = [int(d) for d in input().split()]

sort_d = sorted(d)

abc = sort_d[N//2-1]
arc = sort_d[N//2]

print(arc-abc)