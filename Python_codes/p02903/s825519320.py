h,w,a,b = map(int,input().split())
ans = [[0]*w for i in range(h)]
fl = True

for i in range(a):
    for j in range(b):
        ans[j][i] = 1
        
for i in range(w-a):
    for j in range(h-b):
        ans[b+j][a+i] = 1
        
for i in range(h):
    print(*ans[i],sep = "")