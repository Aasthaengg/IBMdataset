import sys
input = sys.stdin.readline
def main(R,C,K,rcv):
  inf=float('inf')
  dp0=[[-inf,-inf,-inf,0] for _ in range(C)]
  # dp0[i][j]:i列目の時点で残りちょうどj個取れる時の最大値
  rcv.sort(key=lambda x:C*R*x[0]+x[1])
  i=0
  nowc=0
  for j in range(R):
    # j+1行目に対する操作
    # 初期化
    for c in range(C):
      dp0[c][3]=max(dp0[c])
      dp0[c][2]=-inf
      dp0[c][1]=-inf
      dp0[c][0]=-inf
    nowc=0
    while i<K and rcv[i][0]==j+1:
      nextc=rcv[i][1]-1
      for k in range(nowc+1,nextc+1):
        dp0[k][0]=max(dp0[k][0],dp0[nowc][0])
        dp0[k][1]=max(dp0[k][1],dp0[nowc][1])
        dp0[k][2]=max(dp0[k][2],dp0[nowc][2])
      v=rcv[i][2]
      dp0[nextc][0]=max(dp0[nextc][0],dp0[nextc][1]+v)
      dp0[nextc][1]=max(dp0[nextc][1],dp0[nextc][2]+v)
      dp0[nextc][2]=max(dp0[nextc][2],dp0[nextc][3]+v)
      i+=1
      nowc=nextc
    for k in range(nowc+1,C):
      dp0[k][0]=max(dp0[k][0],dp0[nowc][0])
      dp0[k][1]=max(dp0[k][1],dp0[nowc][1])
      dp0[k][2]=max(dp0[k][2],dp0[nowc][2])
    #print(dp0)
  print(max(dp0[-1]))
if __name__=='__main__':
  R,C,K=map(int,input().split())
  rcv=[list(map(int,input().split())) for _ in range(K)]
  main(R,C,K,rcv)
