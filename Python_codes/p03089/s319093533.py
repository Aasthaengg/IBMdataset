N=int(input())
b=list(map(int, input().split()))
a=[]
for i in b:
    if len(a)<i-1:
        print(-1)
        exit()
    a.insert(i-1,i)
for i in a:
    print(i)
