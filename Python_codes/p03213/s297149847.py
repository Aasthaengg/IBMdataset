import math
def C(a,b):
    if a < b:
        return 0
    else:
        return math.factorial(a) // (math.factorial(b)*math.factorial(a-b))

N = int(input())
if N == 1:
    print(0)

else:
    PF = dict()
    for i in range(2, N+1):
        n = i
        for x in PF.keys():
            while n % x == 0:
                n //= x
                PF[x] += 1
        if n != 1:
            PF[n] = 1
    
    count, number = [0]*5, [3, 5, 15, 25, 75]
    for x in PF.values():
        for i in range(5)[::-1]:
            if x + 1 >= number[i]:
                count[i] += 1
                break
    ans = 0
    ans += C(count[0], 1) * C(sum(count[1:]), 2) + 3 * C(sum(count[1:]), 3)
    ans += C(count[1], 1) * C(sum(count[2:]), 1) + 2 *C(sum(count[2:]), 2)
    ans += C(sum(count[:3]), 1) * C(sum(count[3:]), 1) + 2 * C(sum(count[3:]), 2)
    ans += count[4]
    print(ans)