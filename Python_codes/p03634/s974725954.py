import sys
input = sys.stdin.readline
def main():
  n=int(input())
  abc=[list(map(int,input().split())) for _ in range(n-1)]
  q,k=map(int,input().split())
  xy=[list(map(int,input().split())) for _ in range(q)]
  # 頂点kを根とした根付き木。kから各頂点への最短距離を求めてクエリごとに足すだけ。
  ki=[[]for _ in range(n)]
  for a,b,c in abc:
    ki[a-1].append([b-1,c])
    ki[b-1].append([a-1,c])
  kakutei=[0]*n
  kyori=[pow(10,14)]*n
  kyori[k-1]=0
  import heapq
  mikakutei=[[0,k-1]]
  heapq.heapify(mikakutei)
  while len(mikakutei)>0:
    k,i=heapq.heappop(mikakutei)
    if kakutei[i]==1:
      continue
    kakutei[i]=1
    l=ki[i]
    for li in l:
      if kakutei[li[0]]==0:
        kyori[li[0]]=min(kyori[li[0]],k+li[1])
        heapq.heappush(mikakutei,[kyori[li[0]],li[0]])
  for x,y in xy:
    print(kyori[x-1]+kyori[y-1])
    

if __name__=='__main__':
  main()
