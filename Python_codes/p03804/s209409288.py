n, m = map(int,input().split())
A = ['']*n
B = ['']*m
for i in range(n):
    A[i] = input()
for i in range(m):
    B[i] = input()

w_dif = len(A[0])-len(B[0])
w_w = len(B[0])
ans = 'No'
for h in range(n-m+1):
    for w in range(w_dif+1):
        window = [wh[w:w+w_w] for wh in A[h:h+m]]
        if window==B:
            ans = 'Yes'
            break
print(ans)