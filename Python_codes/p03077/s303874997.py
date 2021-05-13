n = int(input())
m = float("inf")

for i in range(5):
    m = min(m,int(input()))
    
print(-(-n//m) + 4)