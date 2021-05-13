n = int(input())
l = []
for i in range(n):
    data = input()
    l.append(data)

ans=0
import re
b_st=0
a_en=0
b_a=0

for tmp in l:
    res = re.findall('AB', tmp)
    ans += len(res)

    a_flg=False
    b_flg=False
    if tmp[0] == "B":
        b_flg=True
    if tmp[-1] == "A":
        a_flg=True

    if b_flg and a_flg:
        b_a+=1
    elif b_flg:
        b_st+=1
    elif a_flg:
        a_en+=1

ans+=min(a_en,b_st)
a_en -= min(a_en,b_st)
b_st -= min(a_en,b_st)

if b_a == 0:
    print(ans)
    exit()
ans+=b_a-1
if a_en != 0 or b_st!= 0:
    print(ans+1)
else:
    print(ans)