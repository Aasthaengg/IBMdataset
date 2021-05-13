# 総和が1ずつ減る
# x,...,xになったら、全部1回ずつ減少対象になったあと
# x-1,...,x-1
# N-1+X,...,N-1+XからNX回でN-1,...,N-1

# ここからr個を巻き戻す
# (N-1+X +N-(r-1)) r個
# (N-1+X -r) N-r個
# at most N-1+X+N <= 10**16+100

K = int(input())
N = 50

x,r = K//N,K%N
a = (N-1+x)+N-(r-1)
b = (N-1+x)-r
answer = [str(a)] * r + [str(b)]*(N-r)
print(N)
print(' '.join(answer))