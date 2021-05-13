N, K = [int(v) for v in input().split(' ')]
A = [int(v) for v in input().split(' ')]

sum_A = sum(A)
max_A = max(A)

def make_divisor(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

div_list = make_divisor(sum_A)
div_list.sort(reverse=True)

for d in div_list:
    R = [a % d for a in A]

    sum_r = sum(R)
    if sum_r % d != 0:
        continue

    R.sort()
    #print("%d: %s" % (d, R))
    flag = False 

    sub = 0
    flag = True
    for i in range(N):
        if flag and sub + R[i] > K:
            flag = False
            #print("%d, i: %d" % (d, i))

        if flag:
            sub += R[i]
        else:
            sub -= (d - R[i])

    #print("%d, sub: %d" % (d, sub))

    if not flag and sub < 0:
        continue

    print(d)
    exit()
