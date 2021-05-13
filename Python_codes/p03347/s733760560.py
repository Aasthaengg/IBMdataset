n=int(input())

a=[int(input()) for _ in range(n)]
#a(n+1)!=0の時、a(n+1)=a(n)+1である

cnt=0

if a[0]!=0:
    print(-1)
    exit()
#print(" ".join(list(map(str,a))))
for ii in range(1,n):
    i=n-ii
    if a[i]==0:
        continue
    elif a[i]<=a[i-1]:
        cnt+=a[i]
    elif a[i]==a[i-1]+1:
        cnt+=1
    elif a[i]>a[i-1]+1 or  a[i]>i:
        print(-1)
        exit()
    #print(b)
    #print(" "*(i+1),"^",cnt)

print(cnt)

    
"""
t: 0 1 1 0 1 2 2 1 2
s: 0 0 0 0 0 0 0 0 0
1: 0 0 1 0 0 0 0 0 0
2: 0 1 1 0 0 0 0 0 0
3: 0 1 1 0 0 0 0 1 0
4: 0 1 1 0 0 0 0 1 2
5: 0 1 1 0 0 1 0 1 2

"""



