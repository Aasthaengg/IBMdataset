n,m = map(int,input().split())
a = list(map(int,input().split()))
homework = sum(a)
ans = n - homework

if ans >= 0 :
    print(n-homework)
else:
    print(-1)