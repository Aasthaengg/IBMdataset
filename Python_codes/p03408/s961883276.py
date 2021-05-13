r1,r2=[input() for _ in range(int(input()))],[input() for _ in range(int(input()))];ans=0
ans=[r1.count(i)-r2.count(i) for i in set(r1)];print(max(0,max(ans)))