# ABC058 B
O = list(input())
E = list(input())
pw = ""

for i in range(len(E)):
    pw = pw + O[i] + E[i]

if len(O) - len(E) == 1:
    pw = pw + O[-1]

print(pw)