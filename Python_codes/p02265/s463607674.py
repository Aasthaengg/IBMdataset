n = int(raw_input())
x = [0 for i in range(n)]
pf = -1
pb = 0

li = []
for i in range(n):
    s = (raw_input().split())
    if s[0] == 'insert':
        pf += 1
        x[pf]=int(s[1])
    elif s[0] == 'delete':
        try:
            p = x[pf::-1].index(int(s[1]))
            x[pf-p] = 0
            while x[pf]==0:
                pf -= 1
            while x[pb]==0:
                pb += 1
        except:
            pass
    elif s[0] == 'deleteFirst':
        x[pf]=0
        pf -= 1
    elif s[0] == 'deleteLast':
        x[pb] = 0
        pb += 1
for e in x[pb:pf+1][::-1]:
    if e != 0:
        print e,