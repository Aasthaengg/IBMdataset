# https://atcoder.jp/contests/tenka1-2018-beginner/tasks/tenka1_2018_d
# D - Crossing

N=int(input())
a=set()
b={}

for i in range(1000):
    if i*(i+1)%2==0:
        s= i*(i+1)//2
        if s<=10**5:
            a.add(s)
            b[s]=i
        else:
            break
            
if N not in a:
    print("No")
else:
    print("Yes")
    print(b[N]+1)
    r=[0 for _ in range(N)] #kaisuu
    t=[ [] for _ in range(b[N]+1)]
    for i in range(b[N]):
        r[i] +=1
    t[0]= [i+1 for i in range(b[N])]
    print(b[N],*t[0])

    for i in range(1,b[N]+1):
        for j in range(i):
            for k,num in enumerate(t[j]):
                if r[num-1]==1:
                    t[i].append(num)
                    r[num-1]+=1
                    break
        for k in range(N):
            if r[k]==0:
                r[k] +=1
                t[i].append(k+1)
                if len(t[i])>=b[N]:
                    break
        print(b[N],*t[i])

        
        
        
        
        #print("i=",i)
        #print(r)
#        for j,num in enumerate(r):
#            if num==1:
#                t[i].append(j+1)
#                r[j]+=1
#                break
        #print("t",t)
        #print(r)
#        for k,num in enumerate(r):
#            if num==0:
#                t[i].append(k+1)
#                r[k]+=1
#            if len(t[i])==b[N]:   
#                break
#        else:
#            pass
#        print(b[N],*t[i])