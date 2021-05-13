n ,m = map(int,input().split())
ok = [False] * n
wa = [0] * n
for i in range(m):
    p,s = input().split()
    if s == 'AC':
        ok[int(p)-1] = True
    elif not(ok[int(p)-1]):
        wa[int(p)-1] += 1
wa_sum = sum([wa[i] * ok[i] for i in range(n)])
print(sum(ok),wa_sum)
