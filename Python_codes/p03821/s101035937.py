num = int(input())
 
A = []
B = []
for i in range(num):
    x,y = map(int,input().split())
    A.append(x)
    B.append(y)
 
val = 0
for i in range(num-1,-1,-1):
    if (A[i]+val)%B[i] == 0:
        pass
    elif A[i] + val > B[i]:
        val += B[i]-((A[i]+val)%B[i])
    else:
        val += B[i]-(A[i]+val)  
print(val)