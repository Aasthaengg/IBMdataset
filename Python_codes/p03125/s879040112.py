ii=lambda:int(input())
miis=lambda:map(int,input().split())
lmiis=lambda:list(map(int,input().split()))

a,b=miis()
print(a+b if b%a==0 else b-a)