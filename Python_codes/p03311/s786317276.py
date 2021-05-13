n=int(input())
a=list(map(int,input().split()))
a=[x-i-1 for i,x in enumerate(a)]
a.sort()
b=a[n//2]
print(sum([abs(x-b) for x in a]))