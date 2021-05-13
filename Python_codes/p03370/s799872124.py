n,x=map(int,input().split())
s=[int(input()) for i in range(n)]
s=sorted(s)

extra=x-sum(s)
extra=extra//s[0]
print(extra+n)