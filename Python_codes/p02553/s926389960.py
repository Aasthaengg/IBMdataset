a,b,c,d=(int(x) for x in input().split())
A=a*c
B=a*d
C=b*c
D=b*d

print(max(A,B,C,D))
