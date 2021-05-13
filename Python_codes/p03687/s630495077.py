import collections
s = input()
sl = collections.Counter(s)
ans = len(s)
s_af = s
for c in sl.keys():
    s_af = s
    cnt = 0
    while s_af.count(c) != len(s_af):
        s_bf = s_af
        cnt +=1
        for i in range(len(s_bf)-1):
            if s_bf[i] ==c or s_bf[i+1]==c:
                if i ==0:
                    s_af = c
                else:
                    s_af += c
            else:
                if i == 0:
                    s_af = s_bf[i]
                else:
                    s_af += s_bf[i]
    ans = min(ans,cnt)

    
print(ans)
