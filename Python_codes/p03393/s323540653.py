s=input()
n=len(s)
cha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
if n<26:
    for i in range(26):
        if s.count(cha[i])==0:
            print(s+cha[i])
            exit()
else:
    for j in range(n-1,0,-1):
        if s[j]>s[j-1]:
            memo=j-1
            break
        if j==1:
            print(-1)
            exit()
    s2=s[:j]
    for i in range(26):
        if s2.count(cha[i])==0 and cha[i]>s[memo]:
            memo2=cha[i]
            break
    print(s[:j-1]+memo2)
