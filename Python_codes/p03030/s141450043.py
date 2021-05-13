N = int(input())
S = [[i + 1] + list(input().split()) for i in range(N)]

for s in sorted(S, key=lambda x: (x[1], -int(x[2]))):
    print(s[0])
