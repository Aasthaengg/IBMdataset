n,m = map(int,input().split())
li = list(map(int,input().split()))
li.sort()
result = 0
for i in range(0,m):
    result += int(li[i])
print(result)