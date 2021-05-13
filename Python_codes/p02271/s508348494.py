n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

def make_list(A):
    n = len(A)
    result = []
    for i in range(2**n):
        tmp = 0
        if i == 0:
            idx = ['0' for _ in range(n)]
        else:
            idx = list(bin(i).lstrip('0b').zfill(n))
        for num, j in enumerate(idx):
            if j == '1':
                tmp += A[num]
        result.append(tmp)
    return result


res = make_list(A)
for i in m:
    if i in res:
        print('yes')
    else:
        print('no')
