_ = input()
s = input()
tmp=0
ans=[0]
for i in s:
    if i == 'D':
        tmp-=1
    else:
        tmp+=1
    ans.append(tmp)
print(max(ans))