s=input()
ans=[0]
atgc=["A","T","G","C"]
for i in range(len(s)):
    for k in range(i,len(s)):
        check=s[i:k+1]
        complete=0
        for i in range(len(check)):
            if check[i] in atgc:
                complete+=1
        if complete==len(check):
            ans.append(len(check))
print(max(ans))