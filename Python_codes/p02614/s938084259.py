h,w,k=map(int,input().split())
c=[0]*h
for i in range(h):
  c[i]=list(str(input()))
l=h+w
ans=0
M = 2#bit探査をしたい時はM=2
def dfs(A):
    global ans
    # 終端条件 --- l 重ループまで回したら処理して打ち切り
    if len(A) == l:
        b=0
        for i in range(h):
          if A[i]==0:
            continue
          else:
            for j in range(w):
              if A[h:l][j]==1 and c[i][j]=='#':
                b+=1
        if b==k:
          ans+=1
        return
    for v in range(M):
        A.append(v)
        dfs(A)
        A.pop() # これが結構ポイント
dfs([])
print(ans)