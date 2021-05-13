n,a,b = map(int,input().split())
L = list(map(int,input().split()))

diff = []
for i in range(n-1):
    diff.append(a*(L[i+1]-L[i]))
#print(diff)
cnt = 0
for i in range(n-1):
    if diff[i] > b:
        cnt +=1
diff.sort()

print(sum(diff[:n-1-cnt]) + b*cnt)