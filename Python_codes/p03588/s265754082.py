N = int(input())
risuto =sorted([tuple(map(int,input().split())) for i in range(N)])
ans = 0
ans += risuto[-1][0] - risuto[0][0]
ans += risuto[-1][1]
ans += risuto[0][0]
print(ans)
