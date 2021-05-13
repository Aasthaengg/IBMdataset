li = list(map(int,input().split()))
li.sort()
sum1 = 0
for i in range(len(li)-1):
    sum1 += abs(li[i+1] - li[i])
print(sum1)