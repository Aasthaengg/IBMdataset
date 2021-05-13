S = list(input())
ans = 0

fst = 0
lst = len(S)-1
flg = 1

while(1):
    if fst>=lst:
        break

    if S[fst]==S[lst]:
        fst += 1
        lst -= 1
        continue
    
    elif S[fst]=="x":
        ans += 1
        fst += 1
    
    elif S[lst]=="x":
        ans += 1
        lst -= 1
    
    else:
        flg = 0
        break

if flg:
    print(ans)
else:
    print(-1)