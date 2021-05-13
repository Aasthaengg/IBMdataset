N = int(input())
mx=0
maxcnt=0
for i in range(1,N+1):
    cnt=0
    while True:
        if i%2==0:
            i/=2
            cnt+=1
        else:
            if cnt>=maxcnt:
                mx=i*2**cnt
                maxcnt=cnt
            break
print(int(mx))
