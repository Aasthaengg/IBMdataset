N = int(input())
p = [int(input()) for _ in range(N)]

p[p.index(max(p))] = int(max(p))/2
print(int(sum(p)))