S = input()
T = input()

ins = -1#挿入場所(できるだけうしろにして前はAでつめる)
for i in range(0,len(S)-len(T)+1,1):
    
    isOk = True
    for j in range(i,i+len(T),1):
        if not(T[j-i]==S[j] or S[j]=="?"):
            isOk = False
            break
        
    if isOk:
        ins = i

if ins == -1:
    print("UNRESTORABLE")
    exit()

ans = list(S)
for i in range(len(T)):
    ans[ins+i]=T[i]

for i in range(len(ans)):
    if ans[i]=="?":
        ans[i]="a"

print("".join(ans))

