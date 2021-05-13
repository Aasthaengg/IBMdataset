n=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
def f(x):
	return l[x]-m[x]
print(sum([f(i) for i in range(n) if f(i)>0]))