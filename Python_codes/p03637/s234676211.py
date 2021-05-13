N=int(input())

S=list(map(int,input().split()))

div1=0
div2=0
div4=0
lenS=len(S)

for i in range(N):
    if S[i]%4==0:
        div4+=1
    elif S[i]%2==0:
        div2+=1
    else:
        div1+=1

if lenS%2==0:

    if div4*2+div2>=lenS:
        print("Yes")
        exit()
    else:
        print("No")
        exit()
else:
    
    if (div4*2+1)>=lenS:
        print("Yes")
        exit()
    elif div4*2+div2>=lenS:
        print("Yes")
        exit()
    else:
        print("No")
        exit()


