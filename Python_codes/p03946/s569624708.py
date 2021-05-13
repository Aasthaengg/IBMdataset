n, t = map(int, input().split())
a = list(map(int, input().split()))
lowest = a[0]
highest = a[0]
baibai = []
for i in range(n):
    if lowest > a[i]:
        lowest = a[i]
    #print(highest, lowest)
    baibai.append(a[i]-lowest)

max_baibai = max(baibai)
ans = baibai.count(max_baibai)
#print(baibai)
print(ans)
