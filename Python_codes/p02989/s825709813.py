N=int(input())
d=list(map(int,input().split()))

d.sort()

th1 = d[N//2-1]
th2 = d[N//2]

print(th2 - th1)
