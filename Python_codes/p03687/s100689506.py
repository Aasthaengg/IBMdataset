from collections import Counter

s = input()

d = Counter(s)
ans = 101

if len(d) == 1:
    print(0)
    exit()

for item in d.keys():
    st = item
    tmp = list(s)
    n = len(s)
#    print('----------',item,tmp,'---------------')
    while n>0:
        gen = []
        flag = True
        for i in range(n-1):
            if tmp[i] == st or tmp[i+1] == st:
                gen.append(st)
            else:
                gen.append(tmp[i])
                flag = False
#        print(gen)
        if flag: break
        else: 
            tmp = gen.copy()
            n -= 1
    ans = min(ans,len(s)-len(gen))
print(ans)