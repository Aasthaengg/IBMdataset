a,b,c = map(int,input().split())
#print(a+b+c)
List =[a,b,c]
x = sorted(List)
#print(x)
if x[0] + x[1] == x[2]:
    print("Yes")
else :
    print("No")