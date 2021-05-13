A, B = map(int, input().split())
cnt=0
for i in range(A,B+1):
    i=str(i)
    a=i[::-1]
    flag=0
    for j in range(len(i)):
        if i[j]!=a[j]:
            flag=1
    if flag==0:
        cnt+=1
print(cnt)

