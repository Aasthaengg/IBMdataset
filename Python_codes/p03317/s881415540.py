n, k = map(int, input().split())

A = list(map(int, input().split()))


min_a = A.index(min(A))

left = min_a
right = n - min_a - 1


min_ = min(left, right)
max_ = max(left, right)


t = 0
min_ = min_ - k
t +=1
temp = 0
if min_ > 0:
    if min_ % (k - 1) != 0:
        temp = min_ // (k - 1)
    else:
        temp = min_ // (k - 1) + 1
    min_ -= temp * (k - 1)
t += temp

max_ = max_ + min_ + 1

if max_ % (k - 1) == 0:
    t += max_ // (k - 1)
else:
    t += max_ // (k - 1) + 1

print(t)