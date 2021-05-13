h,w,a,b=map(int,input().split())
s = [[0 for _ in range(w)] for __ in range(h)]

for i in range(a):
    for j in range(b):
        s[j][i] = 1

for i in range(w-a):
    for j in range(h-b):
        s[b+j][a+i] = 1

for i in range(h):
    print(''.join([str(x) for x in s[i]]))