import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
a = LI()
M,m = max(a),min(a)
b,c = a.index(M)+1,a.index(m)+1

if M > 0 and m < 0:  # 符号を揃える
    print(2*N-1)
    if M <= -m:
        for i in range(1,N+1):
            a[i-1] += m
            print(c,i)
    else:
        for i in range(1,N+1):
            a[i-1] += M
            print(b,i)
else:
    print(N-1)

if max(a) <= 0 :
    for i in range(N,1,-1):
        print(i,i-1)
else:
    for i in range(1,N):
        print(i,i+1)
