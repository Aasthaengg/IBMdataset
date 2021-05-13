n,k,q = map(int,input().split())
point = [k-q for _ in range(n)]
for i in range(q):
    p = int(input())
    point[p-1] += 1
    
for j in point:
    if j > 0:
        print("Yes")
        
    else:
        print("No")