n=int(input())
p = [int(x) for x in input().split()]
q = [int(x) for x in input().split()]

cnt=1

import itertools
for seq in itertools.permutations(range(1,n+1)):
    p_hantei=True
    q_hantei=True
    for i in range(n):
        if p[i]!=seq[i]:
            p_hantei=False
            break
    for i in range(n):
        if q[i]!=seq[i]:
            q_hantei=False
            break

    if p_hantei:
        p_num=cnt
    if q_hantei:
        q_num=cnt

    cnt+=1
print(abs(p_num-q_num))