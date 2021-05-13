N = int(input())
A = list(map(int,input().split()))
p,n = 0,0
Positive,Negative = [],[]
ans = []
for i in range(N):
    if A[i] >= 0:
        p += 1
        Positive.append(A[i])
    else:
        n += 1
        Negative.append(A[i])
Positive.sort()
Negative.sort()
if n == 0:
    now = Positive[0]
    for i in range(1,N-1):
        ans.append((now,Positive[i]))
        now -= Positive[i]
    ans.append((Positive[N-1],now))
    Positive[N-1] -= now
    print(Positive[N-1])
    for i in range(len(ans)):
        print(*ans[i])
elif n >= 1 and p >= 1:
    now = Negative[0]
    for i in range(p-1):
        ans.append((now,Positive[i]))
        now -= Positive[i]
    bigM = now
    now = Positive[-1]
    for i in range(1,n):
        ans.append((now,Negative[i]))
        now -= Negative[i]
    bigP = now
    ans.append((bigP,bigM))
    bigP -= bigM
    print(bigP)
    for i in range(len(ans)):
        print(*ans[i])
else:
    now = Negative[-1]
    for i in range(N-1):
        ans.append((now,Negative[i]))
        now -= Negative[i]
    print(now)
    for i in range(len(ans)):
        print(*ans[i])