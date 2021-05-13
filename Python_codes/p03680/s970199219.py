n = int(input())
a=[0]
for i in range(n):
    a.append(int(input()))
s=1
cnt=0
while s !=2:
    s=a[s]
    cnt +=1
    if cnt ==n:
        print(-1)
        exit()
print(cnt)