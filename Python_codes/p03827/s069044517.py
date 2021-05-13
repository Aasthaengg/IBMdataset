n=int(input())
s=input()
ans=0
num=0
for i in range(n):
    if s[i]=="I":
        num+=1
    else:
        num-=1
    if ans<num:
        ans=num
print(ans)
