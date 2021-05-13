N,T = map(int,input().split())
A = list(map(int,input().split()))
pro = {} #利益がkey売るポイントが何個あるかがvalue
m = A[0]
for i in range(1,N):
    if m > A[i]:
        m = A[i]
    elif A[i]-m not in pro:
        pro[A[i]-m] = 1
    else:
        pro[A[i]-m] += 1

mk = 0
ans = 0
for k, v in pro.items():
    if k > mk:
        mk = k
        ans = v
#print(pro)
print(ans)