N=int(input())

step = sum([90*100**i for i in range(len(str(N))//2)])
dance_floor = sum([9*100**i for i in range(len(str(N))//2)])

ans = len(str(N))%2 * (N-step)  +  -1*(len(str(N))%2-1) * dance_floor
print(ans)
