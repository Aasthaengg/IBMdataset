N, K = map(int, input().split())
A = list(map(int, input().split()))
# A.sort()
totalA = sum(A)
# print (totalA)

def make_divisors(n): #nの約数をO(root(n))で全列挙、sortして取り出すときはO(root(n) log(n))
    import math
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0: #割り切れるとき
            divisors.append(i)
            if i != n//i:
                divisors.append(n//i)
    divisors.sort(reverse = True)
    return divisors

divisors_lst = make_divisors(totalA)
# print (divisors_lst)
for i in divisors_lst: #答えの候補を全探索
    lst = []
    for j in A:
        lst.append(j % i)
    lst.sort()
    total_lst = 0
    for j in lst:
        total_lst += i - j
    tmp = 0
    for k in lst:
        tmp += k
        total_lst -= (i - k)
        if max(tmp, total_lst) <= K:
            print (i)
            exit()
