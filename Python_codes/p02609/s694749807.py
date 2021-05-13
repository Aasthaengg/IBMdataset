n = int(input())
X = input()
x = int(X,2)
bitx = bin(x).count('1')
 
ans = [0]*(bitx+2)
for i in range(1,bitx+2):
    ans[i] = 1 + ans[i%bin(i).count('1')]
#print(ans)
l = []
bitp = bitx + 1
bitm = bitx - 1
xmp = 0
xmm = 0


if bitx != 1:
    for i in range(n):
        if X[i] == '1':
            xmp += pow(2, n-(i+1), bitp)
            xmm += pow(2, n-(i+1), bitm)
    for i in range(n):
        if X[i] == '1':
            xm = (xmm - pow(2,n-i-1,bitm)) % bitm
            l.append(str(1+ans[xm]))
        else:
            xm = (xmp + pow(2,n-i-1,bitp))%bitp
            l.append(str(1+ans[xm]))
 
else:
    for i in range(n):
        if X[i] == '1':
            xmp += pow(2, n-(i+1), bitp)
    for i in range(n):
        if X[i] == '1':
            l.append(str(0))
        else:
            xm = (xmp + pow(2,n-i-1,bitp))%bitp
            l.append(str(1+ans[xm]))
 
print('\n'.join(l))
