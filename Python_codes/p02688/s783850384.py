n,k = list(map(int,input().split()))
sunuke = [i for i in range(1,n+1)]
have = []
for i in range(k):
    d = int(input())
    a = list(map(int,input().split()))
    for i in a:
        have.append(i)

ans = list(set(sunuke) - set(have))
print(len(ans))
