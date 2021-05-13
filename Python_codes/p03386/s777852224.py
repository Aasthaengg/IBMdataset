A,B,K = map(int,input().split())

if B-A > K:
    ax = [i for i in range(A,A+K)]
    bx = [i for i in range(B-K+1,B+1)]
    sum = sorted(list(set(ax + bx))) 
else:
    sum = [i for i in range(A,B+1)]

for i in sum:
    print(i)

