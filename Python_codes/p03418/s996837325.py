n,k = map(int, input().split())
count = 0
for b in range (k+1,n+1):
    
    if (k==0):
        x = (n//b)*(b-k) + max(n%b-k+1,0) -1
    else:    
        x = (n//b)*(b-k) + max(n%b-k+1,0)

    count += x
print(count)