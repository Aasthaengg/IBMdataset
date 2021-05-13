n, k = list(map(int, input().split()))
#from collections import deque
if n < k:
    c = k//2  # 作れるccとsの数
    # print(c)
    # print(c-n)　#nコScc c-nがあまりの分
    # print((c-n)//2)
    print(n+(c-n)//2)
else:
    c = k//2
    print(c)
