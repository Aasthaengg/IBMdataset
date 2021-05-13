S,T = input(),input()
N,M = len(S),len(T)
maximum = 0
maxstr = ""
for i in range(0,N-M+1):
    str = S[:i] + T + S[i+M:]

    n = 0
    for j in range(i,i+M):
        if (S[j] != str[j])&(S[j]!="?"):
            n = 1
            # print(S[j],str[j])
            break
    if n==1:continue

    match = 0
    for j in range(N):
        if (S[j] == str[j])|(S[j]=="?"):match += 1
    if maximum<=match:
        maximum = match
        maxstr = str
    # print(str)
# print(maximum)
if maximum == 0:print("UNRESTORABLE")
else:print(maxstr.replace("?","a"))