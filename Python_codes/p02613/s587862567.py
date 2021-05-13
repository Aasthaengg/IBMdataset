N=int(input())
S=[input() for i in range(N)]
AC_count=0
WA_count=0
TLE_count=0
RE_count=0
for i in range(N):
    if S[i]=="AC":AC_count+=1
    if S[i]=="WA":WA_count+=1
    if S[i]=="TLE":TLE_count+=1
    if S[i]=="RE":RE_count+=1
print("AC x "+str(AC_count))
print("WA x "+str(WA_count))
print("TLE x "+str(TLE_count))
print("RE x "+str(RE_count))