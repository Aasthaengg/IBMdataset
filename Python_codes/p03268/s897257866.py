n,k = map(int,input().split())
count = 0
count += (n//k) ** 3 
if k % 2 == 0:
    count += ((n + k/2) // k) ** 3
print(int(count)) 
