N,M,X = map(int,input().split())
A =  list(map(int,input().split()))
#print(A)
left = []
right = []
for i in A:
    if i > X:
        right.append(i)
    else:
        left.append(i)
    
#print(right,left)
print(min(len(right),len(left)))