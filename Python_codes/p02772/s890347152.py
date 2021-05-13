n = int(input())
a = list(map(int,input().split()))
cnt=0
for i in range(n):
    if a[i]%2==0:
        if a[i]%3==0:
            pass
        elif a[i]%5==0:
            pass
        else:
            cnt+=1
if cnt==0:
    print("APPROVED")
else:
    #print(cnt)
    print("DENIED")