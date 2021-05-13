n = int(input())
A = list(map(int, input().split()))

from collections import deque


cash = 1000
stock = 0

peak_min = deque()
peak_max = deque()

d_prev = 0
for i in range(1, n):
    a = A[i]
    if A[i] > A[i-1]:
        d = 1
    elif A[i] == A[i-1]:
        d = d_prev
    else:
        d = -1
    if d_prev*d == -1:
        if d == 1:
            peak_min.append(i-1)
        elif d == -1:
            peak_max.append(i-1)
    d_prev = d
#print(peak_min, peak_max)

if len(peak_min) == 0 and len(peak_max) == 0:
    if A[0] < A[-1]:
        ans = cash%A[0] + cash//A[0]*A[-1]
    else:
        ans = cash
elif len(peak_min) == 0:
    ans = cash%A[0] + cash//A[0]*A[peak_max[0]]
elif len(peak_max) == 0:
    ans = cash%A[peak_min[0]] + cash//A[peak_min[0]]*A[-1]
else:
    if peak_max[0] < peak_min[0]:
        peak_min.appendleft(0)
    if peak_max[-1] < peak_min[-1]:
        peak_max.append(n-1)
#    print(peak_min, peak_max)
    
    while len(peak_min) != 0:
        i = peak_min.popleft()
        stock += cash//A[i]
        cash = cash%A[i]
#        print(i, cash , stock)
        
        i = peak_max.popleft()
        cash += stock*A[i]
        stock = 0
#        print(i, cash , stock)
    ans = cash
print(ans)