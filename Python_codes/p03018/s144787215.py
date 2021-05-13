from sys import stdin
s = stdin.readline().rstrip()
s = s.replace("BC","D")
point = 0
count = 0
for i in s:
    if i == "A":
        count += 1
    elif i == "D":
        point += count
    else:
        count = 0
print(point)