N=int(input())

print(0,flush=True)
init=input()
if init=="Vacant":
    exit()
print(N-1,flush=True)
ende=input()
if ende=="Vacant":
    exit()

cnt=2
s=0
e=N-1

while cnt<=19:

    c= (s+e)//2
    leng_sc = c-s
    leng_ce = e-c
    print(c,flush=True)
    tmp=input()
    if tmp=="Vacant":
        exit()
    else:        
        if (leng_sc%2==0 and tmp!=init) or (leng_sc%2==1 and tmp==init):
            e = c
            ende = tmp
        else:
            s = c
            init = tmp

    cnt+=1
