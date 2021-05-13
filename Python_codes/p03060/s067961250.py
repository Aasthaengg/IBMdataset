N = int(input())

Vn = list(map(int, input().split()))
Cn = list(map(int, input().split()))


result = 0
temp = 0
for V, C in zip(Vn, Cn):
    temp = V - C
    if temp >= 0:
        result += temp

print(result)

