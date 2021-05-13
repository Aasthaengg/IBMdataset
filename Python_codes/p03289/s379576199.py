S = input()
cond1 = (S[0]=="A")
cond2 = (S[2:len(S)-1].count("C") == 1)


flag = True
if not cond1:
    flag = False
else:
    if not cond2:
        flag = False
    else:
        idx = S[2: len(S)-1].index("C") + 2
        new = S[1:idx] + S[idx+1:]
        if new != new.lower():
            flag = False

if flag:
    print("AC")
else:
    print("WA")
