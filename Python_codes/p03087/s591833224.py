n,q = map(int,input().split())
s = input()
s += ' '
ruiseki = []
i = 0
while i<n:
    if s[i]+s[i+1]=='AC':
        ruiseki.append('')
        ruiseki.append('AC')
        i= i+1
    else:
        ruiseki.append(s[i])
    i+=1
t = [0] * (n+1)
for i in range(n):
    if ruiseki[i] == 'AC':
        t[i+1] = t[i]+1
    else:
        t[i+1] = t[i]
for i in range(q):
    l,r = map(int,input().split())
    print(t[r]-t[l]) 