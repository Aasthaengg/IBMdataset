S = input()
if ord(S[0]) != 65:
    print("WA")
    exit()
num = 0
for i in range(2,len(S)-1):
    if S[i] == "C":
        num = i
if not num:
    print("WA")
    exit()
else:
    for j in range(1,len(S)):
        if j != num:
            if 97 <= ord(S[j]) <= 122:
                continue
            else:
                print("WA")
                exit()
print("AC")