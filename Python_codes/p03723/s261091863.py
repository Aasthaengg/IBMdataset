a, b, c = map(int, input().split())
dic = []
count = 0

while all([a%2 == 0, b%2 == 0, c%2 == 0]):
    a, b, c = int((b+c)/2), int((a+c)/2), int((c+a)/2)
    if (a, b, c) in dic:
        count = -1
        break
    else:
        dic.append((a, b, c))
        count += 1

print(count)