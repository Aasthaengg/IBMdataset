from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

n = inn()
for k in range(n+5):
    m = k*(k-1)//2
    #ddprint("k {} m {}".format(k,m))
    if m>n:
        break
    if m<n:
        continue
    cnt = 1
    s = [ [] for i in range(k) ]
    for i in range(k-1):
        for j in range(i+1,k):
            s[i].append(cnt)
            s[j].append(cnt)
            cnt += 1
    print('Yes')
    print(k)
    for i in range(k):
        printn(k-1)
        for j in s[i]:
            printn(' ' + str(j))
        print('')
    exit()
print('No')
