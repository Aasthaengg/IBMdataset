P = [1 for _ in range(100)]
P[0]=0
P[1]=0
for i in range(2,11):
    for j in range(i**2,100,i):
        P[j] = 0
Q = []
for i in range(100):
    if P[i]==1:
        Q.append(i)
N = int(input())
C = {p:0 for p in Q}
for i in range(2,N+1):
    for p in Q:
        if i%p==0:
            x = i
            while x%p==0:
                x = x//p
                C[p] += 1
cnt = 0
for p in Q:
    if C[p]>=74:
        cnt += 1
cnt1 = 0
cnt2 = 0
for p in Q:
    if C[p]>=24:
        cnt2 += 1
    elif C[p]>=2:
        cnt1 += 1
cnt += cnt2*(cnt2-1)+cnt2*cnt1
cnt1 = 0
cnt2 = 0
for p in Q:
    if C[p]>=14:
        cnt2 += 1
    elif C[p]>=4:
        cnt1 += 1
cnt += cnt2*(cnt2-1)+cnt2*cnt1
cnt1 = 0
cnt2 = 0
for p in Q:
    if C[p]>=4:
        cnt2 += 1
    elif C[p]>=2:
        cnt1 += 1
cnt += (cnt2*(cnt2-1)*(cnt2-2))//2+((cnt2*(cnt2-1))//2)*cnt1
print(cnt)