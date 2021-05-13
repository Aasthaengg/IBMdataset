n=int(input())
ans=[]
for i in range(n):
    a,b=map(str, input().split())
    ans.append([a,int(b)*-1,i+1])

import operator
ans.sort(key=operator.itemgetter(0,1))

for i in range(n):
    print(ans[i][2])