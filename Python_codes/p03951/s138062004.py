#AtCoder Grand Contest 006 a
def check(moji):
    x1=""
    x2=""
    for i in range(n):
        x1+=moji[i]
        x2+=moji[len(moji)-n+i]
    if s==x1 and t==x2:
        return True
    else:
        return False
n=int(input())
s=input()
t=input()
ans=[]
ans.append(s)
for i in range(len(t)-1,-1,-1):
    ans.append(s+t[i:])
for i in ans:
    if check(i):
        print(len(i))
        break
