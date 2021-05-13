t = list(input())


for i in range(len(t)):
    if t[i] == "?":
        t[i] = "D"

answer = "".join(str(n) for n in t)

print(answer)