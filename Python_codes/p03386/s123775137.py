A,B,N=list(map(int,input().split()))
l=set()
for i in range(A,A+N):
    if i > B:
        break
    l.add(i)
for i in reversed(range(B-N+1,B+1)):
    if i < A:
        break
    l.add(i)
l=list(l)
l.sort()
for i in l:
    print(i)