q,h,s,d=map(int,input().split())
n=int(input())

one = min(q*4,h*2,s)
two = min(one*2,d)

print((n//2)*two+(n%2)*one)