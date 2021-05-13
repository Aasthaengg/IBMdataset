N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [0]
D = [0]

for i in range(N):
    s = B[i] - A[i]
    if(s > 0):
        C.append(s)
    elif(s < 0):
        D.append(s)

D = sorted(D)

csum = sum(C)
dsum = sum(D)

if(csum + dsum > 0):
    print(-1)
elif(csum == 0):
    print(0)
else:
    ans = len(C) -1
    for i in D:
        csum += i
        ans += 1
        if(csum <= 0):
            break
    print(ans)