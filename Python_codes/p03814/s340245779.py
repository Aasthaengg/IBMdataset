S = input()
a = []
z = []
for i, s in enumerate(S):
    if s == "A":
        a.append(i)
    elif s == "Z":
        z.append(i)
print(z[-1]-a[0]+1)