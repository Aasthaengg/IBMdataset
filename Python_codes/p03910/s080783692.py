n = int(input())

cnt = 0
for i in range(1,n+1):
    cnt += i
    if cnt >= n:
        idx = i
        break


sum = 0
for i in range(1,idx+1)[::-1]:
    if sum+i < n:
       print(i)
       sum += i
    
    else:
        print(n-sum)
        break
