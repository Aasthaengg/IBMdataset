printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True  and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

h,w = inm()
c = [0]*26
for i in range(h):
    s = ins()
    for j in range(w):
        c[ord(s[j])-ord('a')] += 1
n1 = len([x for x in c if x%2==1])
n2 = len([x for x in c if x%4==2])

ddprint(c)
ddprint(n1)
ddprint(n2)

if h%2==0 and w%2==0:
    print('No' if n1>0 or n2>0 else 'Yes')
elif h%2==1 and w%2==1:
    k = w//2 + h//2
    print('No' if n1!=1 or n2>k else 'Yes')
else:
    k = 0
    if h%2==1:
        k = w//2
    if w%2==1:
        k += h//2
    print('No' if n1!=0 or n2>k else 'Yes')
