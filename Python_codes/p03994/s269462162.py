S=list(input())
k=int(input())
for i in range(len(S)):
    s=S[i]
    if s=="a":continue
    x=123-ord(s)
    #print(s,x,ord("z"))
    if k>=x:
        k-=x
        S[i]="a"

    else:continue
k%=26
for i in range(len(S)):
    if S[-1-i]!="a":
        S[-1-i]=chr((ord(S[-1-i])-97+k%26)+97)
        print("".join(S));break
else:
    S[-1]=chr((ord(S[-1])-97+k%26)+97)
    print("".join(S))