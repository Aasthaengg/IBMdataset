n = int(input())
S = []
for i in range(n):
    S.append(input())
cnt_ac = 0
cnt_tle = 0
cnt_wa = 0
cnt_re = 0


for i in range(n):
    if S[i] == "AC":
        cnt_ac += 1
    elif S[i] == "TLE":
        cnt_tle += 1
    elif S[i] == "WA":
        cnt_wa += 1
    elif S[i] == "RE":
        cnt_re += 1

print("AC x " + str(cnt_ac))
print("WA x " + str(cnt_wa))
print("TLE x " + str(cnt_tle))
print("RE x " + str(cnt_re))