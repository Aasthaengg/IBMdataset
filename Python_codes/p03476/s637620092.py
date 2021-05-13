import math
import bisect
import sys
input = sys.stdin.readline
q = int(input())

def sieve_of_erastosthenes(num):
    input_list = [False if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else True for i in range(num)]
    input_list[0] = input_list[1] = False
    input_list[2] = input_list[3] = input_list[5] = True
    sqrt = math.sqrt(num)

    for serial in range(3, num, 2):

        if serial >= sqrt:
            return input_list

        for s in range(serial ** 2, num, serial): 
            input_list[s] = False

prime = set([i for i, f in enumerate(sieve_of_erastosthenes(10**5)) if f])
like = []
for p in prime:
    if (p+1)//2 in prime:
        like.append(p)
like.sort()

for i in range(q):
    l, r = map(int, input().split())
    st = bisect.bisect_left(like, l)
    en = bisect.bisect_right(like, r)

    print(en-st)