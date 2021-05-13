s=input()
k=int(input())
for i in range(len(s)):
    if s[i]=="1":
        k-=1
    else:
        k-=int(s[i])*(5*10**18)
    if k<=0:
        print(s[i])
        exit()