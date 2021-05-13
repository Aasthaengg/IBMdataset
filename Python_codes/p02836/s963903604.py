S=str(input())
ans=0
for i in range(len(S)//2):
    if S[i]!=S[-i-1]:#S[-i-1]だと後ろからi番目を出力
        ans=ans+1
print(ans)