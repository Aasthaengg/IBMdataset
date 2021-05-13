n,*t=map(int,open(0).read().split());T=sum(t[:n]);q=t[:n:-1]
while q:print(T-t[q.pop()-1]+q.pop())