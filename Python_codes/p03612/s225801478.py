n = int(input())
li = list(map(int,input().split()))
all_li = []
tmp = []
for i,l in enumerate(li):
    if i+1 ==l:
        if len(tmp) == 0:
            tmp.append(l)
        else:
            if tmp[-1] == l-1:
                tmp.append(l)
            else:
                all_li.append(tmp)
                tmp = [l]
    else:
        all_li.append(tmp)
        tmp = []
if len(tmp)>0:
    all_li.append(tmp)
ans = 0
for a in all_li:
    ans += len(a)//2 + len(a)%2        
print(ans)