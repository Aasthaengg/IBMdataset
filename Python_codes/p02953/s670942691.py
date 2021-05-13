n = int(input())
 
h = list(map(int,input().split()))
 
height = h[0]
 
q = 0
 
for i in h:
    if i < height:
        q = 1
        break
    elif i > height:
        height = i-1
    else:
        height = i
        
if q == 1:
    print("No")
else:
    print("Yes")