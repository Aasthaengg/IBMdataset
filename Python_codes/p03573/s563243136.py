a,b,c=map(int,input().split())
print((a==b)*c+(b==c)*a+(c==a)*b)