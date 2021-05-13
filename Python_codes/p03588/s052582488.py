N=int(input())
P=[tuple(map(int,input().split())) for _ in range(N)]
P.sort(key=lambda x: x[0])
a,b=P[-1]
print(a+b)