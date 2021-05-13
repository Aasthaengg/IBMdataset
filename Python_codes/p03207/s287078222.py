# input
N = int(input())
p = [int(input()) for n in range(N)]

max_idx = p.index(max(p))
p[max_idx] //= 2
print(sum(p))