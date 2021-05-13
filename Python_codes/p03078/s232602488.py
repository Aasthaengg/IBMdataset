X,Y,Z,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

# A,B,Cのリストを降順にソート
A.sort(reverse =True)
B.sort(reverse =True)
C.sort(reverse =True)

# A,B,Cを上からp,q,r番目を選択した場合にp*q*rがKより大きい組み合わせがKより上位に来ることはない
# A,B,Cを上から参照していき。p*q*rがK以下の場合はリストにa+b+cを追加，K以上の場合はbreak
D = []
for p in range(1,X+1):
    for q in range(1,Y+1):
        for r in range(1,Z+1):
            if p*q*r<=K:
                D.append(A[p-1]+B[q-1]+C[r-1])
            else:
                break
D.sort(reverse=True)

for i in range(K):
    print(D[i])