n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
s = 0
temp = -100
for i in a:
    s += b[i - 1]
    if temp + 1 == i:
        s += c[temp - 1]
    temp = i
print(s)
