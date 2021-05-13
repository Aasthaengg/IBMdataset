s = int(input())
m = int(1e9)+7
if s < 3:
    ans = 0
else:
    d = [0] * (s+1)
    d[0] = 1
    for i in range(3, s+1):
        for j in range(3, s+1):
            if i>= j:
                d[i] = (d[i] + d[i-j])%m
    ans = d[s]
print(ans)