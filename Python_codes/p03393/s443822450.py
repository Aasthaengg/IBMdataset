s=input()

ans=""

if len(s)<26:
    cnt_alphabet=[0]*26

    for i in range(len(s)):
        cnt_alphabet[ord(s[i])-97]+=1
    
    moji=""
    for i in range(26):
        if cnt_alphabet[i]<1:
            moji=chr(i+97)
            break
    ans=s+moji

else:
    cnt=25
    
    for i in range(24,-1,-1):
        if ord(s[i])>ord(s[i+1]):
            cnt=i
        else:
            break
    
    if cnt==0:
        ans='-1'
    else:
        min_chr=ord('{')
        for m in s[cnt:]:
            if ord(m)>ord(s[cnt-1]):
                min_chr=min(min_chr,ord(m))
            
        ans=s[:cnt-1]+chr(min_chr)

print(ans)