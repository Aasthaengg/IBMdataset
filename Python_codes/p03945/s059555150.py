S = list(input())

check=S[0]
S_=check
for s in S[1:]:
    if check != s:
        check = s
        S_+=check
        
print(len(S_)-1)