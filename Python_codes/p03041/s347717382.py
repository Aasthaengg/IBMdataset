N,K=map(int,input().split())
a=input()
b=list(a)

c=b[K-1]
b[K-1]=c.lower()
print(''.join(map(str,b)))