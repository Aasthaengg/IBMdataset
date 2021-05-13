#入力受け取り
N, K, C=map(int, input().split())
S='x'+input() #インデックスと日数を合わせるために先頭に'x'を追加

#前詰めな働き方の場合で働く日を求める
A=[] #前詰めで働く場合の働く日リスト
i=1 #1日目から判定スタート
while len(A)<K:
  if S[i]=='o':
    #i日目に働けるなら、リストにiを追加し、iをC+1だけ進める
    A.append(i)
    i+=(C+1)
  else:
    #i日目に働けないならその日は働けないので(小泉構文)、iに1足すのみ
    i+=1
    
#後ろ詰めな働き方の場合で働く日を求める
B=[]
i=N #N日目から判定スタート
while len(B)<K:
  if S[i]=='o':
    #i日目に働けるなら、リストにiを追加し、iをC+1だけ戻す
    B.append(i)
    i-=(C+1)
  else:
    #i日目に働けないならその日は働けないので(小泉構文)、iから1引くのみ
    i-=1
    
B=B[::-1] #Bは降順に追加されているので、昇順にする
for i in range(K):
  #i番目に働くのが前詰めと後ろ詰めで同じ日であれば出力
  if A[i]==B[i]:
    print(A[i])
