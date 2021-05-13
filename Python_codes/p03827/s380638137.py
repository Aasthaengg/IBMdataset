N = int(input())
S = input()

x = 0
max_x = 0
for s in S:
    if s =="I":
        x += 1
    else:
        x -= 1
    if x > max_x:
        max_x = x

print(max_x)