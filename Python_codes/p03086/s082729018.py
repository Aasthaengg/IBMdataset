s=input()

ans = 0
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        if s[i:j].count("A")+s[i:j].count("C")+s[i:j].count("G")+s[i:j].count("T")==j-i:
            ans = max(ans,j-i)
print(ans)
