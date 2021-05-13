import heapq

x,y,z,k=map(int,input().split())

A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

q=[(-1*(A[0]+B[0]+C[0]),0,0,0)]

heapq.heapify(q)

used=[[0,0,0]]

a=0
b=0
c=0
cnt=0
while cnt<k:
    p,a,b,c=heapq.heappop(q)
    cnt+=1
    print(p*-1)
    a+=1
    if (not [a,b,c] in used) and a<x:
        heapq.heappush(q,(-A[a]-B[b]-C[c],a,b,c))
        used.append([a,b,c])
    a-=1
    b+=1
    if (not [a,b,c] in used) and b<y:
        heapq.heappush(q,(-A[a]-B[b]-C[c],a,b,c))
        used.append([a,b,c])
    b-=1
    c+=1
    if (not [a,b,c] in used) and c<z:
        heapq.heappush(q,(-A[a]-B[b]-C[c],a,b,c))
        used.append([a,b,c])