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

n,a,b = inm()
v = inl()
v.sort(reverse=True)
ave = sum(v[:a])/a
print(ave)
if v[0]>v[a-1]:
    l = a-1
    while l>0 and v[l-1]==v[a-1]:
        l -= 1
    r = a-1
    while r<n-1 and v[r+1]==v[a-1]:
        r += 1
    dend = sor = 1
    #ddprint(f"a {a} l {l} r {r}")
    # comb(r-l+1, a-l)
    for i in range(a-l):
        dend *= r-l+1-i
        sor *= a-l-i
    p = dend//sor
    #ddprint(f"i {i} dend {dend} sor {sor} inc {dend//sor} p {p}")
else:
    r = a-1
    while r<n-1 and v[r+1]==v[a-1]:
        r += 1
    # c=min(b,r+1), sum< j=a..c >[comb(r+1,j)]
    p = 0
    #ddprint(f"a {a} l {l} r {r}")
    for j in range(a,min(b,r+1)+1):
        dend = sor = 1
        for i in range(j):
            dend *= r+1-i
            sor *= j-i
        p += dend//sor
        #ddprint(f"i {i} dend {dend} sor {sor} inc {dend//sor} p {p}")
print(p)
