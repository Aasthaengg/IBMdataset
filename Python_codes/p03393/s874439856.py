# AGC022 A - Diverse Word
s=input()
n=len(s)
mozi=[0]*26
ans=''
if s=='zyxwvutsrqponmlkjihgfedcba':
    print(-1)
elif n<26:
    for ss in s:
        mozi[ord(ss)-97]+=1
    for i in range(len(mozi)):
        if mozi[i]==0:
            break
    ans=s
    ans+=chr(97+i)
    print(ans)
elif n==26:
    for i in range(1,27):
        if s[-i]>s[-i-1]:
            break
    ss=sorted(s[-i:])
    for sss in ss:
        if sss>s[-i-1]:
            break
    print(s[:-i-1]+sss)
