T = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

d = [(A[i] - B[i])*T[i] for i in range(2)]
if d[0] < 0:
    d = [-d[0],-d[1]]
s = sum(d)
if s == 0:
    print('infinity')
elif s > 0:
    print(0)
else:
    print(d[0]//(-s)*2 + 1 - (d[0]%s == 0))
