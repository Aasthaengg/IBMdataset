n = int(input())

cnt = 0
for a in range(1,n+1):
    if n%a != 0:
        cnt +=n//a
    else:
        cnt +=n//a-1
    #print(a,n//a,cnt)
print(cnt)