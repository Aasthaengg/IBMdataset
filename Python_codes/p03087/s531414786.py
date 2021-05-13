N,Q = list(map(int,input().split()))
s = input()
lis=[0]*N
 
count = 0
for i in range(1,len(s)):
    if s[i-1] == 'A' and s[i] == 'C':
        count +=1
    lis[i]+=count
for i in range(Q):
    l,r = list(map(int,input().split()))
    print(lis[r-1]-lis[l-1])
