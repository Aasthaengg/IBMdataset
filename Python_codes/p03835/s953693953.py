K, S = map(int, input().split())
ans = 0

for x in range(K+1):
    for y in range(K+1):
        z = S - (x+y)
        if(0<=z and z<=K):
            if(x == y and y == z):
                ans += 1
            elif(x != y and y != z and z != x):
                ans += 1
            else:
                ans += 1
                
                
                
print(ans)