s=list(input())
k=int(input())

for i in range(len(s)):
    if k==0:break

    num=ord(s[i])
    ch_num=123-num
    if i==len(s)-1:
        s[i]=chr(97+(num+k-97)%26) #if num+k>122 else chr(num+k)
        #print(97+(num+k-97)%26)
        k=0
        break
    elif s[i]=='a':continue
    elif ch_num<=k:
        s[i]='a'
        k-=ch_num
print(''.join(s))