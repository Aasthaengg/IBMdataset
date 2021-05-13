n, k = map(int,input().split())
d = []
a = []
for i in range(1,k+1):
    d.append(int(input()))
    a_temp = list(map(int,input().split()))
    a.append(a_temp)

num = []
    
for i in range(n):
    cnt = 0
    for j in range(k):
        if i+1 in a[j]:
            cnt += 1
    if cnt == 0:
        num.append(i)
print(len(num))