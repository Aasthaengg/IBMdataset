n,m = map(int,input().split())
a = list(map(int,input().split()));
x = 0;
y = -1;

for i in range(m):
    x += a[i]

if x > n:
    print(y);
else:
    print(n-x);