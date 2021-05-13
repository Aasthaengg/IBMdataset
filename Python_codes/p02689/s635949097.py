N,M = map(int,input().split())
Hls = list(map(int,input().split()))
lst = [[] for i in range(10**5)]
for i in range(M):
    A,B = map(int,input().split())
    lst[A-1].append(Hls[B-1])
    lst[B-1].append(Hls[A-1])
k = 0
for i in range(N):
    if bool(lst[i]):
        if Hls[i] > max(lst[i]):
            k += 1
    else:
        k += 1

print(k)