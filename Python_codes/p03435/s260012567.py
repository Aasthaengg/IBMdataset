c1=list(map(int,input().split()))
c2=list(map(int,input().split()))
c3=list(map(int,input().split()))
if c2[0]-c1[0]==c2[1]-c1[1] and c2[1]-c1[1]==c2[2]-c1[2] and c3[0]-c1[0]==c3[1]-c1[1] and c3[1]-c1[1]==c3[2]-c1[2] :
    print("Yes")
    exit()
print("No")