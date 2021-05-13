n = int(input())
bli = list(map(int,input().split()))
answer = bli[0]
for i in range(1,n-1):
    answer += min(bli[i],bli[i-1])
answer += bli[n-2]
print(answer)