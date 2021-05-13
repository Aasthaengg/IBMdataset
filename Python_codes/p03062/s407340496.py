#D
n = int(input())
a = list(map(int, input().split()))
min = 10e19
sum = 0
count = 0
for i in range(n):
    sum += abs(a[i])
    if abs(a[i]) < min:
        min=abs(a[i])
    if a[i] < 0:
       count += 1
    # print(sum,count,min)
if count % 2 == 0 or count == 0:
    ans = sum
else:
    ans = sum - abs(min * 2)
print(ans)
