a,b,c = map(int,input().split())
x = [a,b,c]
for i in x:
    if x.count(i) == 1:
        print(i)
    
