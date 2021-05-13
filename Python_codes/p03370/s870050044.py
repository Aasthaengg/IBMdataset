n,x=map(int,input().split())
m=[int(input()) for _ in range(n)]
m.sort()
num=x-sum(m)
print(n+(num//(min(m))))
