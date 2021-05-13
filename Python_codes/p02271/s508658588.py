
n = int(raw_input())
A = map(int, raw_input().split())

q = int(raw_input())
M = map(int, raw_input().split())

result = []
for i in range(q):
    result.append('no')

def adder(axis = 0, nums = [0], M = [0], q = 0):
    for i in range(q):
        if M[i] == axis:
            result[i] = 'yes'
    length = len(nums)
    if length != 0:
        for i in range(length):
            sum_n = axis + nums[i]
            adder(sum_n, nums[i+1:], M, q)

for i in range(n):
    adder(A[i], A[i+1:], M, q)

for i in result:
    print(i)