n,m = map(int, input().split())
total=n*m

if n==1 and m==1:
    print(1)
    exit()

if n==1 or m==1:
    print(max(n,m)-2)
else:
    print(max(0, total -((n+m)*2-4)))