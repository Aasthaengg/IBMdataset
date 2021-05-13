N = int(input())
p = [int(input()) for _ in range(N)]
i = max(p) / 2
p.remove(max(p))
p.append(i)
print(int(sum(p)))