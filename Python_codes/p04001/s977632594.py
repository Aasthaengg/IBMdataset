S=str(input())
l=len(S)-1
ans=0

M = 2#bit探査をしたい時はM=2
def dfs(A):
    global ans
    # 終端条件 --- l 重ループまで回したら処理して打ち切り
    if len(A) == l:
        memo=0
        for i in range(l):
            if A[i]==1:
                ans+=int(S[memo:i+1])
                memo=i+1
        ans+=int(S[memo:])
        return
    for v in range(M):
        A.append(v)
        dfs(A)
        A.pop() # これが結構ポイント

dfs([])
print(ans)