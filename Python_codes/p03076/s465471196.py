import math
a = [int(input()) for _ in range(5)]
ans = 0
min0 = 10
for i in a:
    if i%10 != 0:
        i = str(i)
        ans += int(i)+10-int(i[-1])
        min0 = min(int(i[-1]), min0)
    else:
        ans += i
print(ans-10+min0)
