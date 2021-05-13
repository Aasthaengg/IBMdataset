x,a,b=map(int,input().split())
s=abs(x-a)
print('A' if s==min(s,abs(x-b)) else 'B')