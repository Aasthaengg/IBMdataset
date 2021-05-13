S = input()
a = 0
x = 0
j = 0
for i in range(len(S)):
    if S[i] == "A" and a == 0:
        a = 1
    if a == 1:
        j += 1
    if S[i] == "Z" and a == 1:
        x = j
print(x)
