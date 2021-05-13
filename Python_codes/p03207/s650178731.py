n = int(input())
p = [int(input()) for _ in range(n)]
p.sort()
print(p.pop() // 2 + sum(p))