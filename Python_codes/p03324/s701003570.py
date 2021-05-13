d, n = map(int, input().split())
def culc(x):
    if x % 100 != 0:
        return 0
    else:
        cnt = 0
        while x % 100 == 0:
            x //= 100
            cnt +=1
        return cnt            

count = 0

for i in range(1, 1010001):
    if culc(i) == d:
        count += 1
    if count == n:
        print(i)
        break