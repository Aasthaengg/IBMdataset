N = int(input())
l = sorted([int(input()) for _ in range(N)])

s = int(sum(l[0:-1]) + l[-1]/2)
print(s)