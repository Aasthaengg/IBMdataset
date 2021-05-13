s=input()
cnt=0
while(1):
    if cnt>=1 and len(s)%2==0 and s[:(len(s)//2)]==s[(len(s)//2):]:
        print(len(s))
        break
    s=s[:-1]
    cnt+=1