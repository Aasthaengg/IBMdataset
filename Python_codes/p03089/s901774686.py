n = int(input())
b = list(map(int,input().split()))
a = []
for i in b:
    if i == 1:
        a.insert(0,1)
    else:
        if len(a)+1 < i:
            print(-1)
            exit()
        a.insert(i-1,i)
    
for i in a:
    print(i)