n = int(input())
D,X = map(int,input().split())
A = [int(input()) for _ in range(n)]
#print(A)
ref = 0
count = [0]*len(A)
for i in range(len(A)):
    ref = 0
    #print(count[i],A[i],i)
    while True:
        ref = count[i]*A[i]+1
        if ref <= D:
            count[i]+=1
        else:
            break
#print(count)
print(sum(count)+X)