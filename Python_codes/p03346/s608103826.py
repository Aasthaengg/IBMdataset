n = int(input())
p = list(int(input()) for i in range(n))
q =[0]*(n+1)
for i in range(n):
    q[p[i]] = i
maxlen = 1
len =1
for i in range(1,n):
    if q[i] < q[i+1]:
        len +=1
    else:
        maxlen = max(maxlen,len)
        len = 1
maxlen = max(maxlen,len)
print(n-maxlen)