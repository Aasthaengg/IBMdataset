r,D,x2000 = map(int,input().split())
next = x2000 
for i in range(1,11):
    next = r*next - D
    print(next)