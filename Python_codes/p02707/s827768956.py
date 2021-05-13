n = int(input())

a = list(map(int, input().split()))

a.sort()

tmp=0
cnt=0

for bangou in range(1,n+1):
    if tmp<len(a):
        while a[tmp]==bangou:
            cnt+=1
            tmp+=1
            if tmp==len(a):
                break
    print(cnt)
    cnt=0

