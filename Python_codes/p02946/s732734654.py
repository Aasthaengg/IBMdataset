K,X = map(int,input().split())

l = []
for i in range(1,(K-1)*2+2):
    l.append(K+X-i)

l = l[::-1]
for i in l:
    print(i,end=" ")