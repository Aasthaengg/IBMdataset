import bisect
 
n, m = map(int, input().split())
a = list(map(int, input().split()))
bc = []
for i in range(m):
    bc.append(list(map(int, input().split())))
bc.sort(key = lambda x: x[1], reverse = True)
a.sort(reverse = True)
count = 0 
count2 = 0
a2 = [0]
for i in range(n):
    a2.append(a2[-1] + a[i])
a.reverse()
sum_a = 0
for i in range(m):
    num = bc[i][1]
    num2 = bc[i][0]
    temp = n - bisect.bisect_left(a, num)
    count += temp
    count2 += temp
    temp2 = min(num2, n - count2)
    sum_a += num * temp2
    count2 += temp2
    if count2 == n:
        break
    count -= temp
    count2 -= temp
count3 = n - (count2 - count)
sum_a += a2[count3]
print(sum_a)