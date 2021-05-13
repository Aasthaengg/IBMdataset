n,m = map(int,input().split())
acli = [0]*n
wali = [0]*n
acsi = 0
wasi = 0
for i in range(m):
    p,s = map(str,input().split())
    if acli[int(p)-1] == 0:
        if s == 'AC':
            acli[int(p)-1] = 1
            acsi += 1
        elif s == 'WA':
            wali[int(p)-1] += 1
for j in range(n):
    if acli[j] == 1 and wali[j] != 0:
        wasi += wali[j]
print(acsi,wasi)