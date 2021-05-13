N = int(input())
c = str(input())

w = c.count("W")
r = c.count("R")

cnt = 0

for i in range(r):
    if c[i] == "W":
        cnt += 1

print(cnt)