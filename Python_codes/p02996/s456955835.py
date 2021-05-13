N = int(input())
lst = []
for i in range(N):
    A,B = map(int,input().split())
    lst.append([B,A])
    
if N == 1:
    print("Yes" if B - A >= 0 else "No")
    exit()
    
lst.sort()  
left = lst[0][0] - lst[0][1]

for i in range(1,N):
    left = left + (lst[i][0] - lst[i-1][0])
    left -= lst[i][1]
    if left < 0:
        print("No")
        exit()
print("Yes")        