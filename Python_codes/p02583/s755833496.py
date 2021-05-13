n = int(input())
l = list(map(int, input().split()))
cnt = 0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            if  l[i] + l[j] > l[k] and l[i] < l[j] + l[k] and l[i] + l[k] > l[j] and l[i] != l[j] and l[i] != l[k] and l[j] != l[k]:
                cnt += 1
print(cnt)