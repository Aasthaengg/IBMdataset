S = input()
if S[0] == "A":
    S_cpy = S.lstrip("A")
else:
    print("WA")
    exit()

if S[2:-1].count("C") == 1:
    S_cpy = S_cpy.replace("C", "")
else: 
    print("WA")
    exit()

if S_cpy.islower():
    print("AC")
else:
    print("WA")