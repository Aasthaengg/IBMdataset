import sys

def call(n):
    nums = []
    for i in range(1, n + 1):
        if i % 3 == 0:
            nums.append(str(i))
            continue
        x = i
        while x > 0:
            if x % 10 == 3:
                nums.append(str(i))
                break
            x = int(x / 10)
    print('', ' '.join(nums))

n = int(sys.stdin.readline())
call(n)