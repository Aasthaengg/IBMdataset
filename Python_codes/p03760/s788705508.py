o = input()
e = input()

for i in range(len(e)):
    print(f"{o[i]}{e[i]}", end="")

if len(o) != len(e):
    print(o[-1])