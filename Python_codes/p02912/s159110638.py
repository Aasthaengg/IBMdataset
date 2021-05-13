[N,M] = list(map(int,input().split()))
A = list(map(int,input().split()))
out=sum(A)
import heapq
a = list(map(lambda x: x*(-1), A))  # 各要素を-1倍 最大値取り出すため
heapq.heapify(a)
# print(a)

for i in range(M):
    # saidai = max(A)
    saidai = heapq.heappop(a)*(-1)
    out-=saidai
    out+=saidai//2
    # A[A.index(saidai)] = saidai//2
    heapq.heappush(a, (saidai//2)*(-1))
    # print('dam,out,a:',saidai,out,a)

print(out)
