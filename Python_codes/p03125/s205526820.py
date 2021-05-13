AB=input().split()
if int(AB[1])%int(AB[0])==0:
    print(int(AB[0])+int(AB[1]))
else:
    print(int(AB[1])-int(AB[0]))