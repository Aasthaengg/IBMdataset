n = int(input())
d = list(map(int,input().split()))

S = sum(d)
T = sum(x*x for x in d)

print((S*S-T)//2)