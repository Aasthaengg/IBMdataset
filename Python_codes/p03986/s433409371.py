x = input()
n = len(x)
s = 0
t = 0
cou = 0

for i in range(n):
    if x[i] == "S":
        s += 1
    elif x[i]== "T":
        if s >= 1:
            s -= 1
            cou += 1
print(n - cou * 2)