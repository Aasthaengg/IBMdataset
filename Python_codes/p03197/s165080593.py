n=int(input())
cnt=0
for i in range(n):
    a=int(input())
    cnt+=(a%2)
if cnt==0:
    print("second")    
else:
    print("first")
