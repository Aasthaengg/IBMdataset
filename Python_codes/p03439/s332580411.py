import sys
d={"Vacant":0, "Male":1, "Female":-1}

N=int(input())
M=[2 for _ in range(N+1)]
print(0, flush=True)
M[0]=d[input()]
M[N]=M[0]

def search(l,r):
    if r - l == 2:
        print(l+1)
        sys.exit()
    print((l+r)//2, flush=True)
    return d[input()]
l=0
r=N
while True:
    m=(r+l)//2
    M[m] = search(l,r)
    if M[m] == 0:
        print(m)
        sys.exit()
    if (m-l) % 2 == 0:
        if M[m] == M[l]:
            l=m
        else:
            r=m
    else:
        if M[m] == M[l]:
            r=m
        else:
            l=m