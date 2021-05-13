N = int(input())

tak = 1
aok = 1

for _ in range(N):
    t, a = map(int, input().split())
    d = max(-(-aok // a), -(-tak // t))
    tak, aok = t * d, a * d

print(tak + aok)