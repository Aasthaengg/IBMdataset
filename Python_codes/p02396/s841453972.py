# coding: utf-8
# Your code here!
# TP1_3_B

# N=input()
# print(N)
N=-1
# while N != 0:
#     N=int(input())
#     print(N)
for i in range(1,10001):
    N=int(input())
    if N == 0:
        break
    print('Case {0}: {1}'.format(i,N))
