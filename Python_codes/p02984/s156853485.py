n = int(input())
a = list(map(int, input().split()))
s = sum(a) - sum(a[1::2]) * 2
print(s)
for i in a[:-1]:
    j = (2*i)-s
    print(j)
    s = j