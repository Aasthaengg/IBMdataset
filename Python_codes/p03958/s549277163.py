k,t = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse = True)
x = sum(a[1:])
y = a[0]

print(max(0,y-x-1))