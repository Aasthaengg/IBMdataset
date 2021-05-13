a, b, t = map(int, input().split())
c = 0
for number in range(1, 21):
    if a * number < t + 0.5:
        c += b
    else:
        pass
print(c)
