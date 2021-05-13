n = int(input())
v = map(int, input().split())
c = map(int, input().split())

surplus = [v - c for v, c in zip(v, c)]
surplus = [v for v in surplus if v > 0]
print(sum(surplus))