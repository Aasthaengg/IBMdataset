def inputlist(): return [int(j) for j in input().split()]
N,X,T =inputlist()
a = (N//X) + int(N % X != 0)
print(a*T)