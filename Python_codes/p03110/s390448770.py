
N = int(input())
xy = [input().split() for i in range(N)]


calculate_yen = lambda xyi: int(xyi[0]) if xyi[1] == 'JPY' else float(xyi[0]) * 380000.0
total = sum(map(calculate_yen, xy))

print(total)
