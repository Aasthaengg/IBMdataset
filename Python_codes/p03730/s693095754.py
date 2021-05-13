A,B,C=map(int,input().split())
remainders=[]
n=1
while True:
    tmp=(A*n)%B
    if not tmp in remainders:
        remainders.append(tmp)
        n+=1
    else:
        break

remainders.sort()
if C==0:
    print("YES")
else:
    if len(remainders)==1:
        print("NO")
    else:
        if remainders[1]==1:
            print("YES")
        else:
            if C%remainders[1]==0:
                print("YES")
            else:
                print("NO")