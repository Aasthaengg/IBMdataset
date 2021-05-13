a,b,c,d = map(int,input().split())
s1 = a*c
s2 = a*d
s3 = b*c
s4 = b*d
print(max(s1,s2,s3,s4))