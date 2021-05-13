a,b,k = map(int,input().split())
num = []

if b-a <= k:
    for i in range(a,b+1):
        print(i)
else:
    for i in range(a,a+k):
        num.append(i)
    for i in range(b-k+1,b+1):
        num.append(i)
        
    num = list(set(num))
    num.sort()
    
    for i in num:
        print(i)

