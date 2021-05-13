n,k=map(int,input().split())
s=input()
c=s.count
print(n-1-max(c('LR')+c('RL')-k*2,0))