r1,r2=[input() for _ in range(int(input()))],[input() for _ in range(int(input()))]
print(max(0,max([r1.count(i)-r2.count(i) for i in set(r1)])))