s=str(input())
ans=0
if s==s[::-1] and s[:(len(s)-1)//2]==s[(len(s)-1)//2-1::-1] and s[(len(s)+3)//2-1:]==s[:(len(s)+3)//2-2:-1]:
    ans+=1
print("NYoe s"[ans::2])