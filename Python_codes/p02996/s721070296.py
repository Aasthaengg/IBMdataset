n = int(input())
L = []
for i in range(n):
    a,b = map(int,input().split())
    L.append((b,a))
L.sort()    
#print(L)
t = 0
for i in range(n):
    t +=L[i][1]
    #print(t,L[i][0])
    if t > L[i][0]:
        print("No")
        exit()
print("Yes")