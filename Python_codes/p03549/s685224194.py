N, M = map(int, input().split())

ans = 0

for i in range(1, 100000):
    p = ((1/2)**M)*(1-(1/2)**M)**(i-1)
    ans += (100*(N-M) + 1900*M)*i*p

print(round(ans))