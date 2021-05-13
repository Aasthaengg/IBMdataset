def prime(num):
    if num == 0:
        return False
    elif num == 1:
        return False
    elif num == 2:
        return True
    i = 2
    while True:
        if i**2 > num:
            break
        if num%i==0:
            return False
        i += 1
    return True
n = int(raw_input())

nums = []
for _ in range(n):
    a = int(raw_input())
    nums.append(a)

ret = 0
for num in nums:
    if prime(num):
        ret += 1
print ret