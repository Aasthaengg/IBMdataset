S = input()

if len(S) > 9:
    print("NO")
    exit()
if not (S.count("K") == 1 and S.count("I") == 1 and S.count("H") == 1 and S.count("B") == 1 and S.count("R") == 1):
    print("NO")
    exit()
if "AA" in S or "KA" in S or "IA" in S:
    print("NO")
    exit()
S = S.replace("A", "")
if not S == "KIHBR":
    print("NO")
    exit()
print("YES")
