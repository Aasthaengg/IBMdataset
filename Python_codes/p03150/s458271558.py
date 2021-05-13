S=input()
length=len(S)
ans='NO'
if S[0:7]=='keyence':
    ans='YES'
elif S[-7:]=='keyence':
    ans='YES'
elif S[0]=='k' and S[-6:]=='eyence':
    ans='YES'
elif S[0:2]=='ke' and S[-5:]=='yence':
    ans='YES'
elif S[0:3]=='key' and S[-4:]=='ence':
    ans='YES'
elif S[0:4]=='keye' and S[-3:]=='nce':
    ans='YES'
elif S[0:5]=='keyen' and S[-2:]=='ce':
    ans='YES'
elif S[0:6]=='keyenc' and S[-1:]=='e':
    ans='YES'

print(ans)