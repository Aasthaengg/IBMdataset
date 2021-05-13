N = int(input())
s =[str(input()) for _ in range(N)]
M = int(input())
t =[str(input()) for _ in range(M)]

l = list(set(s))


mx  = max(s.count(l[i])-t.count(l[i]) for i in range(len(l)))
print(max(0,mx))