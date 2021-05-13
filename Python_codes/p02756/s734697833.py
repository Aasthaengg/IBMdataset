s=input()
n=int(input())
cnt=0
left=[]
right=[]
for _ in range(n):
    tmp=input()
    if tmp[0]=="1":
        cnt+=1
    else:
        num,side,st=tmp.split()
        if side=="1":
            if cnt%2==0:
                left.append(st)
            else:
                right.append(st)
        else:
            if cnt%2==0:
                right.append(st)
            else:
                left.append(st)
left="".join(left)
left=left[::-1]
right="".join(right)
s=left+s+right
if cnt%2==1:
    s=s[::-1]
print(s)