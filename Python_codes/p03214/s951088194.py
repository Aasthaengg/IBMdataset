n,a=int(input()),list(map(int,input().split()))
b=[abs(i-sum(a)/n) for i in a]
c=[i for i in range(n) if b[i]==min(b)]
print(c[0])