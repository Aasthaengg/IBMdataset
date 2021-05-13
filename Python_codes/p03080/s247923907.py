n = int(input())
a = list(input())
r = b = 0
for i in a:
    if i == "R":
        r +=1
    else:
        b += 1

print("Yes") if r > b else print("No")