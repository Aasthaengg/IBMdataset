n = int(input())
c = input()
red = 0
white = 0
for i in range(n):
    if c[i] == "R":
        red += 1
for i in range(red):
    if c[i] == "W":
        white += 1
print(white)
