n,x = map(int,input().split())
m = [int(input()) for i in range(n)]
m.sort()
x = x-sum(m)
if m[0]>x:
    print(n)
else:
    print(n+(x//m[0]))