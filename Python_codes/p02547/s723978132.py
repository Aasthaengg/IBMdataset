N = int(input())
count=0
for i in range(N):
    a, b = map(int, input().split())
    if a == b:
        count +=1
    else:
        count=0
    
    if count ==3:
        print("Yes")
        break
    
    if i == N-1:
        print("No")