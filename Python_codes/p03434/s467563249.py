n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
b = len(a)
a_sum = 0
b_sum = 0
for i in range(b):
    if i % 2 == 0:
        a_sum = a_sum + a.pop(0)
    else:
        b_sum = b_sum + a.pop(0)
print(a_sum-b_sum)