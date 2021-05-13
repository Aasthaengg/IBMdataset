X = int(input())
S = 100
year = 0
while True:
    if S >= X:
        print(year)
        quit()
    S += S // 100
    year += 1
