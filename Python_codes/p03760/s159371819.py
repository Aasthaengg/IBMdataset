O = list(input())
E = list(input())
pw = ""

if len(O) != len(E):
    for i in range(len(O)-1):
        pw += O[i]+E[i]
        if i == len(O)-2:
            pw += O[len(O)-1]
else:
    for j in range(len(O)):
        pw += O[j]+E[j]

print(pw)