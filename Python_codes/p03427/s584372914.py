a=list(input());x,y=len(a)-1,int(a[0]);print(9*x+y if all(i=='9'for i in a[1:])else y-1+9*x)