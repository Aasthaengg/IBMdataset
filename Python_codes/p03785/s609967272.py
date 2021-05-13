import bisect

N, C, K = map(int,input().split())

T = [0]*N
for i in range(N):
    T[i] = int(input())
T.sort()


#print(T)

ans = 0
left = 0
while True:
    if left >= N:
        break
    #print("T[left]",T[left])
    ind = bisect.bisect_right(T, T[left]+K)
    #print("ind",ind)
    left = min(ind, left+C)
    ans += 1
    #print("left",left)
    #print('&&&&&&&&&&&&&&&&&&')
    
print(ans)