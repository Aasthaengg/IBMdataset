S = input()
day = 15 - len(S)
print("YES") if S.count("o") + day >= 8 else print("NO")
