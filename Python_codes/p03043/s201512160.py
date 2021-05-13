import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,K = LI()

prob = []
for i in range(1,N+1):
    if i >= K:
        prob.append(1)
    else:
        a = 0
        while i*2**a < K:
            a += 1
        prob.append(1/2**a)

print(sum(prob)/N)