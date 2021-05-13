N, M = [int(s) for s in input().split(' ')]
ac = 0
wa = 0
result = dict()
fail = dict()
for m in range(M):
    p, s = input().split(' ')
    if p in result and result[p] == 'AC':
        continue
    if s == 'WA':
        fail[p] = fail.get(p, 0) + 1
        result[p] = s
    elif s == 'AC': # AC
        ac += 1
        wa += fail.get(p, 0) 
        result[p] = s
    
print(str(ac) + ' ' + str(wa))
