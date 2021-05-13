def check(n):
    count = 0
    for i in range(1, n + 1):
        if(n % i == 0):
            count += 1
    if(count == 8 and n % 2 != 0):
        return True
    else:
        return False


n = int(input())
count = 0
for i in range(1, n + 1):
    if(check(i)):
        count += 1
print(count)
