pair = input()
t = pair.split(" ")
t = list(map(int, t))
innerRating = 0

if t[0] >= 10:
    innerRating = t[1]
else:
    innerRating = t[1] + 100*(10 - t[0])

print(innerRating)
