q,h,s,d = map(int,input().split())
n = int(input())
s = min(q*4,h*2,s)
d = min(s*2,d)
print(s if n==1 else (n//2)*d+(n%2)*s)