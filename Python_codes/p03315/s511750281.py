S = input()

c = 0

for i in range(4):
    if S[i] == "+":
        c += 1
    else:
        c -= 1

print(c)