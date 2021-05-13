r,d,x = map(int,input().split())
a = [r*x-d]*10
for i in range(1,len(a)):
    a[i] = r*a[i-1]-d
for ans in a:
    print(ans)
