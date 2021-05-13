S = input()
s0 = S[0]
for s in S[1:]:
    if s == s0:
        print("Bad")
        exit()
    s0 = s
print("Good")