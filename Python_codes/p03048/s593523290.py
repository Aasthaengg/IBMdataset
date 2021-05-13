r,g,b,n = map(int, input().split())
ans = 0
#print('i,r,j,g,k,b')
r,g,b = sorted([r,g,b], reverse=True)
for i in range(n//r+1):
    for j in range((n-r*i)//g+1):
        k = n-i*r-j*g
        #print(i,r,j,g,k,b, '===', i+j+k, i*r + j*g + k*b)
        if k%b==0:
            ans += 1
print(ans)