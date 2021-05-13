n,c=map(int,input().split())

import heapq  # heapqライブラリのimport
tv=[-1]
heapq.heapify(tv)  # リストを優先度付きキューへ
#print(heapq.heappop(a))  # 最小値の取り出し
#heapq.heappush(a, -2)
ch=[0]*c

stc=[]
for _ in range(n):
    s,t,c=map(int,input().split())
    stc.append((s,t,c))

stc.sort()

for item in stc:
    s,t,c=item[0],item[1],item[2]
    temp=heapq.heappop(tv)
    if temp<s:
        heapq.heappush(tv,t)
    elif temp==s and ch[c-1]==temp:
        heapq.heappush(tv, t)
    else:
        heapq.heappush(tv,temp)
        heapq.heappush(tv,t)
    ch[c-1]=t
    #print(tv)
print(len(tv))


