combined = input().split(" ")
n = int(combined[0])
r = int(combined[1])

if n >= 10:
    print(r)
else:
    print(r + 100 * (10 - n))
