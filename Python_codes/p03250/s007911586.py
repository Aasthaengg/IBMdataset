a,b,c = map(int,input().split())

X =a*10 + b + c
Y =b*10 + a + c
Z =c*10 + a + b
ans =max(X,Y,Z)
print(ans)