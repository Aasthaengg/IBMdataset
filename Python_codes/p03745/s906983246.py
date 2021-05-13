N = int(input())
A = list(map(int,input().split()))
cur = 0
cnt = 0
while cur<N:
    cnt += 1
    c = 0
    cur1 = cur+1
    for i in range(cur+1,N):
        if A[i]>=A[i-1]:
            cur1 = i+1
        else:
            cur1 = i
            break
    cur2 = cur+1
    for i in range(cur+1,N):
        if A[i]<=A[i-1]:
            cur2 = i+1
        else:
            cur2 = i
            break
    cur = max(cur1,cur2)
print(cnt)