r,g,b,n= map(int,input().split())
R = n//r
G = n // g
B = n // b
ans =0
for i in range(R+2):
    for j in range(G+2):
        if n - (i*r+j*g)< 0:
            continue
        if (n - (i*r+j*g) )%b ==0 and n - (i*r+j*g)>=0:
            ans +=1
print(ans)