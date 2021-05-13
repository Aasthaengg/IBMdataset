a,b=map(int,input().split())
print(min(max(b-a,-b+a+2),abs(a+b)+1))