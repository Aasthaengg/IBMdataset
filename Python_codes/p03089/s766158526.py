# 操作を逆順に考える
# j番目の数がjなら取り除ける
# 取り除けるものが複数ある場合、最も右のを取り除かないと、番号がズレて取り除けなくなる
# 1,2,3
# 1を取り除くと
# 2,3になってダメ
# 順番に操作して、逆順に出力

N=int(input())
b=list(map(int,input().split()))

ans=[]
while len(b)>0:
  for i in range(len(b)-1,-1,-1):
    if b[i]==i+1:
      ans.append(i+1)
      del b[i]
      break
  else:
    print(-1)
    exit(0)
for i in range(len(ans)-1,-1,-1):
  print(ans[i])