from sys import stdout
printn = lambda x: stdout.write(x)
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
DBG = True  and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

n,m = inm()
s = input().strip()
seq = [n]
p = n
while p>0:
    ddprint("p {}".format(p))
    p0 = p
    for i in range(max(0,p-m),p):
        if s[i]=='0':
            ddprint("add {}".format(i))
            seq.append(i)
            p = i
            break
    if p==p0:
        print(-1)
        exit()
seq.reverse()
for i in range(len(seq)-1):
    printn(str(seq[i+1]-seq[i])+' ')
print('')
