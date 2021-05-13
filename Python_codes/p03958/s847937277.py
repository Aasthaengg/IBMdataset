k,t = map(int,input().split())
a = list(map(int,input().split()))
m = max(a)
print(max(0,2*m-sum(a)-1))