s=str(input())
word=["A","C","G","T"]
con,ans=0,0
for i in range(len(s)):
    if s[i] in word:
        for x in range(len(s)-i):
            if s[i+x] in word:
                con+=1
            else:
                break
        if con > ans:
            ans=con
        con=0
print(ans)