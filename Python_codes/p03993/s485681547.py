n = int(input())

a = list(map(int,input().split()))

res = 0

for i,v in enumerate(a,1):
    if i == a[v-1]:
        res += 1
print(res//2)