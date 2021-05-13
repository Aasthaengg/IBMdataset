n = int(input())
A = [0]*n
for i in range(n):
    count = 0
    flg_odd = 0
    l = i
    i = i+1
    while(True):
        if ( i%2 != 0):
            flg_odd = 1
        if ( flg_odd == 1):
            A[l] = count
            break
        i = i//2
        count += 1
m = A.index(max(A))
print(m+1)