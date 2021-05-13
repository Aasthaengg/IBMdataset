n = int(input())
v = list(map(int, input().split()))
v.sort()
ave = v[0]
for i in range(1,n):
    ave += v[i]
    ave = ave / 2
print(ave)
