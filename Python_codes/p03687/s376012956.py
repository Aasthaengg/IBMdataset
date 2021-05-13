printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

s = ins()
mx = [0]*26
cur = [0]*26
for c in s:
    for j in range(26):
        d = chr(ord('a')+j)
        if c==d:
            cur[j] = 0
        else:
            cur[j] += 1
            mx[j] = max(mx[j],cur[j])
    #ddprint(f"c {c}")
    #ddprint(cur)
    #ddprint(mx)
print(min(mx))
