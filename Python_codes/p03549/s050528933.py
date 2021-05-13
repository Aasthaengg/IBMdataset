N, M = map(int, input().split())

ans = 0
for i in range(1, 10**5):
    ans += ((1-(1/2)**M)**(i-1)) * ((1/2)**M) * (1900*M+100*(N-M)) * i

print(int(round(ans, -2)))