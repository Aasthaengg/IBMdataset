N = int(input())

a = list(map(int,input().split()))

a.sort()


x = []
i = len(a)-1
#print(a)

while i > 0:
    if a[i] == a[i-1]:
        x.append(a[i])
        i-=1

    i-=1
    
    if len(x) == 2:
        print(x[0]*x[1])
        exit()



print(0)


