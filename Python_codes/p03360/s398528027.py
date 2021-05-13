num = list(map(int,input().split()))
for i in range(int(input())):
    tmp = max(num)
    num[num.index(tmp)] = tmp*2
print(sum(num))
