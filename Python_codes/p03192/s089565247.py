n=int(input())
cnt=0
while n >= 1:
    if n%10==2:
        cnt+=1
    n=int(n/10)
print(cnt)