o = input()
e = input()
for i in range(max(len(o), len(e))):
    # print(len(o), len(e), i)
    if len(o) > i:
         print(o[i], end="", sep="")
    if len(e) > i:
         print(e[i], end="", sep="")
print()