n=int(input())
*a,=map(int,input().split())
a.sort()
print(abs(a[-1]-a[0]))