H,W=map(int,input().split())
a=[]

for i in range(H):
    a.extend(list(input()))

b=[0]*26
abc="abcdefghijklmnopqrstuvwxyz"

for i in a:
    b[abc.index(i)]+=1

if max(b)==H*W:
    print("Yes")
    exit()


num_odd=0
num_4=0
num_2=0

for i in range(26):
    if b[i]%4!=0:
        if b[i]%2==1:
            if num_odd!=0:
                print("No")
                exit()
            else:
                num_odd=b[i]
        else:
            num_4+=4*(b[i]//4)
            num_2+=b[i]%4
    else:
        num_4+=b[i]

if H%2==0 and W%2==0:
    if num_odd!=0 or num_2!=0:
        print("No")
    else:
        print("Yes")
elif H%2==1 and W%2==0:
    if num_4-(H-1)*W>=0 and num_4-(H-1)*W+num_2==W:
        print("Yes")
    else:
        print("No")
elif H%2==0 and W%2==1:
    if num_4-(W-1)*H>=0 and num_4-(W-1)*H+num_2==H:
        print("Yes")
    else:
        print("No")
elif H%2==1 and W%2==1:
    if num_4+4*(num_odd//4)>=(H-1)*(W-1):
        print("Yes")
    else:print("No")