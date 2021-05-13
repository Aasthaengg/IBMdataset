n = int(input())
l = []
la = l.append
for _ in range(n): l.append(list(map(int, input().split())))
l = list(map(lambda x: x[1] - x[0] + 1, l))
print(sum(l))