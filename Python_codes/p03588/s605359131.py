n = int(input())
AB = [list(map(int, input().split())) for _ in range(n)]
AB.sort(key=lambda ab: ab[1])
print(AB[-1][0] - 1 + AB[0][1] + (AB[0][0] - AB[-1][0] + 1))
