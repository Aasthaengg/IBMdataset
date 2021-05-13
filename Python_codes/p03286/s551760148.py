N=int(input())
# 例外のN=0について
if N==0:
    print(0)
    exit()

a=1
b=0
up=[a]
low=[b]
ct=1
while not b<=N<=a:
    if ct%2==0:
        a+=(-2)**ct
    else:
        b+=(-2)**ct
    ct+=1
    up.append(a)
    low.append(b)
# print(ct)
# print(up)
# print(low)

# 頭の桁から決める
ans=['0']*ct
r=N
for i in range(ct-1):
    # print(low[ct-i-2], up[ct-i-2], r-(-2)**(ct-i-1))
    tmp=r-(-2)**(ct-i-1)
    if low[ct-i-2]<=tmp<=up[ct-i-2]:
        ans[i]='1'
        r=tmp
ans[ct-1]=str(r)
# print(ans)

print((''.join(ans)))