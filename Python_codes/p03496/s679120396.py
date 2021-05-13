def get_min_idx_val(A, N):
    min_val = A[0]
    min_idx = 0
    for i in range(N):
        if min_val > A[i]:
            min_val = A[i]
            min_idx = i
            
    return min_idx, min_val

def get_max_idx_val(A, N):
    max_val = A[0]
    max_idx = 0
    for i in range(N):
        if max_val < A[i]:
            max_val = A[i]
            max_idx = i
            
    return max_idx, max_val

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    min_idx, min_A = get_min_idx_val(A, N)
    max_idx, max_A = get_max_idx_val(A, N)
    sign = 0
    if abs(min_A) <= abs(max_A):
        sign = 1
    else:
        sign = -1
            
    ret = 0
    query = []
    # print('sign:',sign)
    additive_idx = max_idx if sign > 0 else min_idx
    additive_val = max_A if sign > 0 else min_A 
    # print(min_idx, max_idx, additive_idx, additive_val)
    for i in range(N):
        if A[i]*sign < 0:
            ret += 1
            query.append('{0} {1}'.format(additive_idx+1, i+1))
            A[i] += additive_val
    
    if sign > 0:
        for i in range(1,N):
            first = i-1
            second = i
            if A[first] > A[second]:
                # if A[second] >= 0:
                ret += 1
                query.append('{0} {1}'.format(first+1, second+1))
                A[second] += A[first]
    elif sign < 0:
        for i in range(0,N-1)[::-1]:
            first = i
            second = i+1
            # print(first, second, A[first], A[second])
            if A[first] > A[second]:
                # if A[first] <= 0:
                ret += 1
                query.append('{0} {1}'.format(second+1, first+1))
                A[first] += A[second]
    
    # print(A)
    output = """{0}
{1}""".format(ret, '\n'.join(query))
    print(output)
    
solve()