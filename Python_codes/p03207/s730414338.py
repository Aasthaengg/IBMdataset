N = int(input())
p = [int(input()) for _ in range(N)]
p.sort()
p[-1] = p[-1]/2
print(int(sum(p)))
