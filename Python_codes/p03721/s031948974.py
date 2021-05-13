N,K = map(int,input().split())
nums = [0]*(10**5+1)
for i in range(N):
    a,b = map(int,input().split())
    nums[a] += b
c = 0
for i in range(1,10**5+1):
    c += nums[i]
    if c >= K:
        print(i)
        exit()
