N,M = map(int,input().split())
homework = list(map(int,input().split()))

hell = sum(homework)

if N - hell >=0:
    print(N - hell)
else:
    print(-1)