import sys
n,m=map(int,input().split())
S=list(map(int,list(input())))
if m > n:
    m = n
idx = n
ans=[]
while idx > 0:
    for i in range(1,m+1)[::-1]:
        #print(i,idx,idx-i,S[idx-i])
        if S[idx-i] == 0 and idx-i>=0:
            idx -= i
            ans.append(i)
            break
    else:
        print(-1)
        sys.exit()
print(*ans[::-1])