N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))
h = []
for i in range(N):
    if i == 0:
        h.append(1)
    elif i == N - 1:
        h.append(1)
    else:
        if T[i] > T[i - 1]:
            h.append(1)
            if T[i] > A[i]:
                h[i] = 0
                break
        elif A[i] > A[i + 1]:
            h.append(1)
            if A[i] > T[i]:
                h[i] = 0
                break
        else:
            h.append(min([A[i], T[i]]))

if max(T) != max(A):
    h.append(0)
    
cnt = 1
for i in range(len(h)):
    cnt *= h[i]
    cnt %= 1000000007
                     
print(cnt % 1000000007)