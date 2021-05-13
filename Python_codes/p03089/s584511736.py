n = int(input())
L = list(map(int,input().split()))
li = []
a = 0
while a <= 101:
    for i in range(len(L)-1,-1,-1):
        if i == L[i]-1:
            li.append(L[i])
            L.pop(i)
            break
    a +=1
    
if len(L) > 0:
    print(-1)
else:        
    li = li[::-1]
    for i in range(len(li)):
        print(li[i])