S = input().rstrip()
cnt = 0
for s in S[2:-1]:
    if s == "C":
        cnt += 1
    else:
        if not s.islower():
            print("WA")
            exit()
if cnt == 1 and S[0] == "A" and S[1].islower() and S[-1].islower():
    print("AC")
else:
    print("WA")