h,w,lim = map(int,input().split())
S = []
ans = 10**10
for i in range(h):
    S.append(input())
for i in range(2**(h-1)):
    bit = ''
    cur = 1
    for j in range(h-1):
        if i&cur != 0:
            bit = '1'+bit
        else:
            bit = '0'+bit
        cur *= 2
    group = []
    if i == 0:
        group = [[i for i in range(h)]]
    else:
        div = []
        for j in range(len(bit)):
            if bit[j] == '0':
                div.append(j)
            else:
                div.append(j)
                group.append(div)
                div = []
        div.append(j+1)
        if len(div) != 0:
            group.append(div)
    num = [0]*len(group)
    cur = len(group)-1
    flag1 = True
    for j in range(w):
        next = [0]*len(group)
        flag2 = True
        for k in range(len(group)):
            plus = 0
            for l in range(len(group[k])):
                if S[group[k][l]][j] == '1':
                    plus += 1
            if plus > lim:
                flag1 = False
                break
            elif plus+num[k] > lim:
                flag2 = False
                next[k] += plus
            else:
                next[k] += plus
        if flag1 == False:
            break
        else:
            if flag2 == False:
                cur += 1
                num = next
            else:
                for k in range(len(group)):
                    num[k] += next[k]
    if flag1:
        ans = min(ans, cur)
print(ans)
