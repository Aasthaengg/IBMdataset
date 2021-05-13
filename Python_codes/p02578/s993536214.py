n = int(input())
a = list(map(int,input().split()))
max_ = 0
sum_ = 0
for i in range(n):
    if max_ < a[i]:
        max_ = a[i]
    else:
        sum_ += max_ - a[i]
print(sum_)