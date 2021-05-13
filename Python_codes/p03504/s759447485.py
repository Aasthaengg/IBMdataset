maxlen = 10**5+1
n, channel = [ int(v) for v in input().split() ]
use_list = [ [ 0 for i in range(maxlen) ] for i in range(channel) ]

for i in range(n):
    a, b, c = [ int(v) for v in input().split() ]
    for j in range(a,b+1):
        use_list[c-1][j] = 1


ans = 0
for i in range(maxlen):
    max_at_i = sum([ use_list[j][i] for j in range(channel) ])
    ans = max(max_at_i,ans)
print(ans)