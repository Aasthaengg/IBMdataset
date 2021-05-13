n = int(input())
a = list(map(lambda x: int(x),input().split()))

count = 0
ans = ""

max_num = max(a)
max_idx = a.index(max_num)
min_num = min(a)
min_idx = a.index(min_num)

if abs(max_num) >= abs(min_num):
    for i in range(len(a)):
        a[i] += max_num
        ans += "{} {}\n".format(max_idx+1, i+1)
        count += 1
    for i in range(len(a)-1):
        a[i+1] += a[i]
        ans += "{} {}\n".format(i+1, i+1+1)
        count += 1
else:
    for i in range(len(a)):
        a[i] += min_num
        ans += "{} {}\n".format(min_idx+1, i+1)
        count += 1
    for i in range(len(a)-1):
        a[len(a)-(i+2)] += a[len(a)-(i+1)]
        ans += "{} {}\n".format(len(a)-(i+1)+1, len(a)-(i+2)+1)
        count += 1
print(count)
print(ans)