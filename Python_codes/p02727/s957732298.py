import bisect
def bisect_left_reverse(a, x):
    if a[0] <= x:
        return 0
    if x < a[-1]:
        return len(a)
    ok = len(a) - 1
    ng = 0
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if a[mid] <= x:
            ok = mid
        else:
            ng = mid
    return ok
X,Y,A,B,C = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
r = list(map(int,input().split()))
p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)
A = p[:X]+q[:Y]
B = []
A.sort(reverse=True)
for i in range(len(r)):
    n = r[i]
    if A[0] == 0:
      break
    if A[-1] < n:
        index = bisect_left_reverse(A,n)
        A.pop(-1)
        B.append(n)
    else:
        break
print(sum(A)+sum(B))