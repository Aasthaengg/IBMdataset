n = int(input())
hl = list(map(int,input().split()))

lst = []
cnt = 0
for i in range(1,n):
    if hl[i-1] >= hl[i]:
        cnt +=1
    else:
        lst.append(cnt)
        cnt = 0
lst.append(cnt)
print(max(lst))
