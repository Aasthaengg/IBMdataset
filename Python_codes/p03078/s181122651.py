X,Y,Z,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

# A,B,Cのリストを降順にソート
A.sort(reverse =True)
B.sort(reverse =True)
C.sort(reverse =True)

from heapq import heappush,heappop
hq = []
arg_hash={}
# キューに追加された組み合わせ
val = A[0]+B[0]+C[0]
# valは初期値(最大値)
heappush(hq,(-val,0,0,0))

for i in range(K):
    ans,a,b,c = heappop(hq)
    # heappopで一番大きい値を取り出す
    print(-ans)
    
    arg_a = (a+1,b,c)
    arg_b = (a,b+1,c)
    arg_c = (a,b,c+1)
    # (a,b,c)の次に大きい組み合わせは(a+1,b,c),(a,b+1,c),(a,b,c+1)のいずれか
    
    if a<X-1 and arg_a not in arg_hash:
        arg_hash[arg_a] = 1
        heappush(hq,(-(A[a+1]+B[b]+C[c]),)+arg_a)
    if b<Y-1 and arg_b not in arg_hash:
        arg_hash[arg_b] = 1
        heappush(hq,(-(A[a]+B[b+1]+C[c]),)+arg_b)
    if c<Z-1 and arg_c not in arg_hash:
        arg_hash[arg_c] = 1
        heappush(hq,(-(A[a]+B[b]+C[c+1]),)+arg_c)