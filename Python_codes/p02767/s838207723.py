N=int(input())
X=map(int, input().split())
X = list(X)


avg = sum(X) / N
avgi = int(avg + 0.5)

ans = 0
for i in X:
#    print((i-avgi)*(i-avgi))
    ans += (i-avgi)**2

print(ans)
