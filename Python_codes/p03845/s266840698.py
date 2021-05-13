n,*t=map(int,open(0).read().split());q=t[:n:-1]
while q:print(sum(t[:n])-t[q.pop()-1]+q.pop())