import sys

MOD = 10**9 + 7

def read_int():
    line = sys.stdin.readline().rstrip('\n')
    return int(line)

def read_int_list():
    line = sys.stdin.readline().rstrip('\n')
    return [int(e) for e in line.split(' ')]

def sign(n):
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0

def prod(A, K, add, remove):
    prod = 1
    for i in range(K):
        if i == remove:
            continue
        prod *= abs(A[i])
        prod %= MOD
    if add != None:
        prod *= abs(A[add])
        prod %= MOD
    return prod

N, K = read_int_list()
A = read_int_list()

A.sort(key=lambda i: -abs(i))

last_plus = None
last_minus = None
sig = 1
for i in range(K):
    sig *= sign(A[i])
    if A[i] > 0:
        last_plus = i
    if A[i] < 0:
        last_minus = i
remove_plus = None
add_plus = None
remove_minus = None
add_minus = None
if sig < 0:
    for i in range(K, N):
        if A[i] > 0 and last_minus != None and remove_minus == None:
            remove_minus = last_minus
            add_minus = i
            sig = 1
        elif A[i] < 0 and last_plus != None and remove_plus == None:
            remove_plus = last_plus
            add_plus = i
            sig = 1
        elif A[i] == 0:
            if sig < 0:
                sig = 0
            break

if sig == 0:
    print(0)
elif sig > 0:
    if remove_plus != None and remove_minus != None:
        if abs(A[remove_plus]*A[add_minus]) > abs(A[remove_minus]*A[add_plus]):
            ap = prod(A, K, add_minus, remove_minus)
        else:
            ap = prod(A, K, add_plus, remove_plus)
    elif remove_plus != None:
        ap = prod(A, K, add_plus, remove_plus)
    else:
        ap = prod(A, K, add_minus, remove_minus)
    print(ap)
else:
    ap = prod(A[::-1], K, None, None)
    print((MOD-ap) % MOD)
