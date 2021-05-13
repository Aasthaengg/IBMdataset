def f(n):return 0 if n<2 else n+f(n/2)+f(n-n/2)
n=f(input())
print " ".join(sorted(raw_input().split(),key=int))
print n