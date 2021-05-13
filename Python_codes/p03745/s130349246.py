n = int(input())
A = list(map(int, input().split()))

#%%
flag = None
up = False
down = False
ans = 1
base = A[0]

for i in range(1, n):
    if base < A[i]:
        up = True
        base = A[i]
    elif base > A[i]:
        down = True
    if (up == True) and (down == True):
        up = False
        down = False
        ans += 1
    base = A[i]
    
print(ans)
