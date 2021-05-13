inp = list(map(int,input().split()))
N = inp[0]
A = inp[1]
B = inp[2]
l=list()
for i in range(N+1):
    n0 = i % 10
    n1 = (i % 100 - n0) // 10
    n2 = (i % 1000 - n0 - n1*10) // 100
    n3 = (i % 10000 - n0 - n1*10 - n2*100) // 1000
    n4 = (i % 100000 - n0 - n1*10 - n2*100 - n3*1000) // 10000
    if A <= n0+n1+n2+n3+n4 <= B:
        l.append(i)
print(sum(l))