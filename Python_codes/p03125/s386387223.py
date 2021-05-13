a,b=map(int,input().split())
print(a+b if a%b==0 or b%a==0 else abs(a-b))