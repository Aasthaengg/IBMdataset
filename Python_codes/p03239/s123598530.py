n, t = map(int, input().split())
apple = [list(input().split()) for _ in range(n)]
orange = []
for i, j  in zip(apple, range(n)):
    if int(apple[j][1]) <= t:
        orange.append(int(apple[j][0]))
    else:
        pass
print(min(orange) if len(orange) > 0 else "TLE")