import heapq

X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)


def calc(p):
    cnt = 0
    for a in A:
        for b in B:
            for c in C:
                if a + b + c < p:
                    break
                cnt += 1
                if cnt >= K:
                    return True
    return False


end = A[0] + B[0] + C[0] + 1
start = 0
while end - start > 1:
    mid = (end + start)//2
    if calc(mid):
        start = mid
    else:
        end = mid

D = []

for a in A:
    for b in B:
        for c in C:
            if a + b + c < start:
                break
            D.append(a + b + c)
D.sort(reverse=True)
for d in D[:K]:
    print(d)
