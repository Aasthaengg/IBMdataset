s = input()
l = s.replace("BC","D").replace("B"," ")
L = l.replace("C"," ").split()
ans = 0
for i in L:
    numa = 0
    for j in i:
        if j == "A":
            numa += 1
        else:
            ans += numa
print(ans)