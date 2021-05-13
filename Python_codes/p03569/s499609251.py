import numpy as np

S = np.array(list(input()))
num_x = np.count_nonzero(S == 'x')
# print(f'{num_x=}')
A = [s for s in S if s != 'x']
# print(f'{S=}, {A=}')

if len(A) % 2 == 0:
    L = A[:len(A) // 2]
    R = A[len(A) // 2:][::-1]
else:
    L = A[:len(A) // 2]
    R = A[len(A) // 2 + 1:][::-1]
# print(f'{L=}, {R=}')
if not np.all(L == R):
    print(-1)
    exit()
# if len(L) == 0 and len(R) == 0:
#     print(0)
#     exit()

reverse_S = S[::-1]
i = 0
j = 0
# 真ん中までSとreverse_Sを進めていってXの数が足りない分それぞれ足す
# x以外の文字でsplitをする？'x' '' 'x' ''

T = []
subset = ''
for s in S:
    # print(f'{subset=}')
    if s == 'x':
        subset += 'x'
    else:
        T.append(subset)
        subset = ''
T.append(subset)
len_T = np.array([len(t) for t in T])
# print(f'{T=}, {len_T=}, {len_T - len_T[::-1]}')
ans = np.abs(len_T - len_T[::-1]).sum() // 2
print(ans)
