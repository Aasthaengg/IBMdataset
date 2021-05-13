N=int(input())
c=input()
j_L=0
j_R=len(c)-1
ans=0
while True:
    while j_L<len(c) and c[j_L]=="R":j_L+=1
    while j_R>=0 and c[j_R]=="W":j_R-=1
    if j_L>=j_R:
        print(ans)
        exit()
    else:
        ans+=1
        j_L+=1
        j_R-=1


