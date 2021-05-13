import itertools

n = int(input())

p = [int(i) for i in input().split()]
q = [int(i) for i in input().split()]

init = sorted(p)


# print(p, q, init)
countp, countq, count = 0, 0, 0

for array in itertools.permutations(init, n):
    # print(array)
    count += 1
    if(list(array) == p):
        countp = count
    if(list(array) == q):
        countq = count


print(abs(countp-countq))
