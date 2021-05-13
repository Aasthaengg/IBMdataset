import sys
def input():
    return sys.stdin.readline()[:-1]
n=int(input())
tmp=1
while 1:
    if 2*n==(tmp+1)*tmp:
        break
    if 2*n<(tmp+1)*tmp:
        print("No")
        exit()
    tmp+=1
print("Yes")
print(tmp+1)
ans=[[] for i in range(tmp)]
a=1
for i in range(tmp):
    for j in range(i+1):
        ans[i].append(a)
        a+=1
# print(ans)
for i in range(tmp):
    b=str(tmp)
    flag=-1
    for j in range(tmp):
        if flag==-1:
            b+=" "+str(ans[i][j])
        else:
            b+=" "+str(ans[i+j-flag][i])
        if j+1==len(ans[i]):
            flag=j
    print(b)
b=str(tmp)
for i in range(tmp):
    b+=" "+str(ans[i][-1])
print(b)