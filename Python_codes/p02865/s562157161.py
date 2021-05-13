s=int(input())

cnt=0
if s%2==0:
    cnt=s//2-1
elif s%2!=0:
    cnt=s//2
print(cnt)