N = int(input())
p = sorted([int(input()) for i in range(N)])
p[-1] = p[-1] // 2
print(sum(p))
