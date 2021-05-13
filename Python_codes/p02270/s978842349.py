num, count = map(int, input().split())
baggages = [int(input()) for _ in range(num)]

def check(capacity):
    index = 0
    for _ in range(count):
        weight = 0
        while weight + baggages[index] <= capacity:
            weight += baggages[index]
            index  += 1

            if index == num:
                return num
    return index


L,R = 0, 100000*10000
while R - L > 1:
    pivot = (L + R) // 2
    v = check(pivot)
    if v >= num:
        R = pivot
    else:
        L = pivot
print(R)
