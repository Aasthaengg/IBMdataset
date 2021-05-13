y, m, d = map(int, input().split('/'))
print("Heisei" if (y == 2019 and m <= 4) or y < 2019 else "TBD")