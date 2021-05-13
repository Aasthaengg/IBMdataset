n = int(input())
t = list(map(int,input().split()))
m = int(input())

for i in range(m):
    p,x = list(map(int,input().split()))
    a = t.copy()
    a[p-1] = x
    print(sum(a))
