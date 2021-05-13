#https://atcoder.jp/contests/arc061/tasks/arc061_a

s=input()
n=len(s)

num=0
for i in range(2**(n-1)):
    flag=[]

    for j in range(n-1):
        if (i>>j)&1:
            flag.append(j)

    if len(flag)==0:
        num+=int(s)
        #print(int(s))
    else:
        for i in range(len(flag)):
            flag[i]+=1
        flag.insert(0,0)
        flag_num=len(flag)
        for k in range(flag_num-1):
            num+=int(s[flag[k]:flag[k+1]])
            #print(int(s[flag[k]:flag[k+1]]))
        num+=int(s[flag[-1]:])
        #print(int(s[flag[-1]:]))

print(num)

