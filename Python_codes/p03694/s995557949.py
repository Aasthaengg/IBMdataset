N=int(input())
a=list(map(int,input().split()))
a.sort()
print(abs(a[len(a)-1]-a[0]))