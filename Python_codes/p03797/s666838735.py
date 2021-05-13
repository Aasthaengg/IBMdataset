N,M = map(int,input().split())

counter=0
#まずあるものでsccを作る
raw_scc=min(N//1,M//2)
N-=raw_scc
M-=raw_scc*2
counter+=raw_scc

#のこったcだけで作る
counter+=M//4
print(counter)