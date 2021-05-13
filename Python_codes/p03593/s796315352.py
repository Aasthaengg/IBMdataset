import heapq

h,w=map(int,input().split())

a=[input() for _ in range(h)]

alphabet={}

for i in range(h):
    for j in range(w):
        if a[i][j] in alphabet:
            alphabet[a[i][j]]+=1
        else:
            alphabet[a[i][j]]=1

same=[-x for x in alphabet.values()]
heapq.heapify(same)

cnt={}

for i in range(h):
    for j in range(w):
        hh=min(i,h-i-1)
        ww=min(j,w-j-1)

        if (hh,ww) in cnt:
            cnt[(hh,ww)]+=1
        else:
            cnt[(hh,ww)]=1

cntv=sorted(cnt.values())

while cntv:
    c=heapq.heappop(same)
    c=-c
    ccnt=cntv.pop()

    if ccnt>c:
        print('No')
        exit(0)
    elif ccnt<c:
        heapq.heappush(same,ccnt-c)

print('Yes')