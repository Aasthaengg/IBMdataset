N = int(input())
AB = []
for _ in range(N):
    AB.append(tuple(map(int, input().split())))

AB = sorted(AB, key = lambda el:sum(el), reverse = True)
#print(AB)

ans = 0
for i in range(0, N):
    if i % 2 == 0:
       ans += AB[i][0]
    else:
        ans -= AB[i][1]
print(ans)
