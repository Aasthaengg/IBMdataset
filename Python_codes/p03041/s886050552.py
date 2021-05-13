(a,b)=list(map(int, input().split()))
s=input()
print(''.join([c if i!=b-1 else c.lower() for i,c in enumerate(s)]))