S=int(input())    
a=S%(10**9)
b=(10**9-a)%(10**9)
print(0,0,1,10**9,(S+b)//(10**9),b)