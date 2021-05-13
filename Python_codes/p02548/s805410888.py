N = int(input())
ans = 0
for i in range(1,N):
    #print((N-0.5)//i)
    ans += (N-1) // i
print(ans)