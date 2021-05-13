n = int(input())

p = [int(input()) for _ in range(n)]

print(int(sorted(p)[-1]*0.5+sum(sorted(p)[:-1])))