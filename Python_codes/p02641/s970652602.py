X,N = map(int,input().split())
p = set(list(map(int,input().split())))

for i in range(101):
    if X-i not in p:
        print(X-i)
        break
    elif X+i not in p:
        print(X+i)
        break
    

