n, q = map(int, input().split())
s = input()
l_r = [ list(map(int, input().split())) for _ in range(q) ]

memo = [0] * (n+1)


for i in range(n):
    if s[i:i+2] == 'AC':
         memo[i+1] = memo[i] + 1
    else:
         memo[i+1] = memo[i]

for l,r in l_r:
    print(memo[r-1]-memo[l-1])