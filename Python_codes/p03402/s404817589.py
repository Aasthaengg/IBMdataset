A, B = list(map(int,input().split()))
K = 50
field = [["" for j in range(2*K)] for i in range(2*K)]
ans = int(0)

for i in range(2*K):
    for j in range(K):
        field[i][j] = "."
    for j in range(K,2*K):
        field[i][j] = "#"
#for i in field:
#    print(*i)
n = int(0)
j = int(0)
while(j<K/2):
    i= int(0)
    while(i<K and n<B-1):
        field[2*i][2*j] = "#"
        i +=1
        n +=1
    j +=1


n = int(0)
j = int(K/2)
while(j<K):
    i= int(0)
    while(i<K and n<A-1):
        field[2*i][2*j+1] = "."
        i +=1
        n +=1
    j +=1

print(2*K,2*K)
for i in field:
#    print(i)
    print(*i,sep="")
#    a = str(i).replace(",", "")
#    print(a)
