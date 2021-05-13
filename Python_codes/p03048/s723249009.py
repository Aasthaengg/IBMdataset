r,g,b,n = map(int,input().split(" "))
count = 0
for i in range(0,n+1,r):
    for j in range(0,n+1,g):
        if i + j <= n:
            if (n - (i + j)) % b == 0: 
                    count += 1
print(count)