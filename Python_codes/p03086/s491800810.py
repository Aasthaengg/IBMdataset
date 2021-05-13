s = input()
S = ""
for i in s:
    if i in "ACGT":
        S+="1"
    else:
        S+="0"
        
ans = max(list(map(len,S.split("0"))))
print(ans)