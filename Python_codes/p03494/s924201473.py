n = int(input())
a_n = [int(i) for i in input().split()]

def is_all_even(nums):
    for n in nums:
        if n % 2 == 1:
            return False
    return True

ret = 0
while is_all_even(a_n):
    i = 0
    for a in a_n:
        a_n[i] = a / 2
        i += 1
    ret += 1

print(ret)
