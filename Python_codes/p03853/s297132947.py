h,w=map(int,input().split())
c=[0]*h
for i in range(h):
    c[i]=list(map(str,input().split()))
for i in range(h):
    for j in range(2):
        print(''.join(c[i]))