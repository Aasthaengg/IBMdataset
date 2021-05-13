d, n = map(int, input().split())
def division(x):
    if x % 100 != 0:
        return 0
    else:
        return division(x//100) +1
count= 0
for i in range(1, 1010001):
    if division(i) == d:
        count +=1
    if count == n:
        print(i)
        break