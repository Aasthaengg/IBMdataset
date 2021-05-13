n=input().split()
P=int(n[0])
Q=int(n[1])
R=int(n[2])
a=P+Q
b=Q+R
c=P+R
print(min(a, b, c))