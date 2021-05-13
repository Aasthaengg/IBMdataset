import copy
s = input()
ans=10000
for i in range(26):
    now = chr(97+i)
    a = copy.copy(s)
   # print(a)
    count=0
    while len(set(a))!=1:
        a_now=""
        for i in range(len(a)-1):
            if a[i] == now or a[i+1] == now:
                a_now += now
            else:
                a_now += a[i]
        #print(a_now)
        a = copy.copy(a_now)
        count+=1
    #print(count,chr(97+i))
    ans=min(ans,count)
print(ans)