num = [int(e) for e in input().split()]
N=num[0]
K=num[1]
if N%K==0:
    print(0)
else:
    print(1)