import sys
from collections import defaultdict
dic = defaultdict(list)
s = input()
t = input()
n = len(s)
for i in range(n):
    dic[s[i]].append(i+1)

#print(dic)

for i in t:
    if dic[i]==[]:
        print(-1)
        sys.exit()
        
ans = dic[t[0]][0]

if len(t)==1:
    print(ans)
    sys.exit()

count=0
#print(ans)
for i in range(1, len(t)):
    #print("ans:{}, count:{}, n:{}".format(ans, count, n))
    if ans >= dic[t[i]][-1]:
        count += 1
        ans = dic[t[i]][0]
    elif ans < dic[t[i]][0]:
        ans = dic[t[i]][0]
    else:
        sm = 0
        la = len(dic[t[i]])-1
        while sm+1<la:
            mi = (sm + la)//2
            if ans >= dic[t[i]][mi]:
                sm = mi
            else:
                la = mi
        ans = dic[t[i]][la]
#print("ans:{}, count:{}, n:{}".format(ans, count, n))
print(ans+count*n)

