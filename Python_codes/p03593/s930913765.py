h,w=map(int,input().split())
l=[chr(i) for i in range(97, 97+26)]
d={i:j for i,j in zip(l,range(26))}
c=[0]*26
for i in range(h):
    s=input()
    for j in s:
        c[d[j]]+=1
if h%2==0 and w%2==0:
    if all([i%4==0 for i in c]):#偶数×偶数のとき、全てが4の倍数でなければならない
        print("Yes")
    else:print("No")
else:
    k=(h//2)*(w//2)
    if h%2==1 and w%2==1:
        if sum([i%2 for i in c])==1:
            if h==1 or w==1:
                print("Yes") 
            elif sum([i//4 for i in c])>=k:
                print("Yes")
            else:print("No")
        else:
            print("No")
    else:
        if sum([i%2 for i in c])==0:
            if h==1 or w==1:
                print("Yes")
            elif sum([i//4 for i in c])>=k:
                print("Yes")
            else:print("No")
        else:print("No")