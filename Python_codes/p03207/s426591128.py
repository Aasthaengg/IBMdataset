N=int(input())
p=[int(input()) for _ in range(N)]

p = sorted(p)
print(p[-1]//2+sum(p[:-1]))