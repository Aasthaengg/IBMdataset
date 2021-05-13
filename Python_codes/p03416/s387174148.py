A,B=map(int,input().split())

K=0
for x in range(A,B+1):
    if str(x)==str(x)[::-1]:
        K+=1
print(K)
