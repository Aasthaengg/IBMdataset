n = input()
A = input().split(' ')
A.sort()
A.reverse()
q = input()
M = input().split(' ')

A = list(map(int,A))
M = list(map(int,M))
A.sort()

A_sum = [0]
for a in A:
    A_sum.append(a+A_sum[-1])
A_sum.pop(0)

A.reverse()
A_sum.reverse()


#memo = [True]*(len(A))

def search(base, m, n):
    if base == m:
        return True
    if len(A)-1 < n or m - base > A_sum[n]:
        return False
    result = False
    for i in range(len(A)-1,n-1,-1):
        if base + A[i] <= m: # and memo[i]:
#           memo[i] = False
#           print(str(A[i]) + ',' + str(base+A[i]) + ',')
            if search(base+A[i], m, i+1):
                return True
#           memo[i] = True
    return result

def print_yn(result):
    if result:
        print('yes')
    else:
        print('no')

for m in M:
#   print(str(m)+':')
    print_yn(search(0,m,0))