n=int(input())
a=list(map(int, input().split()))
a.sort()
acc=0
cnt=1
for i in range(n-1):
    acc+=a[i]
    if 2*acc<a[i+1]:
        cnt=1
    else:
        cnt+=1
    # print(acc, cnt)
print(cnt)
