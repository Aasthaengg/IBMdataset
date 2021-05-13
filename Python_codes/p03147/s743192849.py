n = int(input())
h = list(map(int,input().split()))
ans = 0
i = 0

while True:
    if max(h) == 0:
        break
    while i < n:
        if h[i] != 0:
            for j in range(i,n):
                if h[j] == 0:
                    #print(j)
                    break
                h[j] -= 1
            #print(h)
            ans += 1
        else:
            i += 1

print(ans)
                
