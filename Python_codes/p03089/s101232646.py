import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N,*A = map(int,read().split())

"""
・任意の i に対して A[i] <= i が必要
・このときできる。次のようにすればよい
・A[i] = i となる 最大の i を取り除く（i=1が満たすので存在）。帰納法がまわってできる。
"""

bl = all(x <= i for i,x in enumerate(A,1))
if not bl:
    print(-1)
    exit()

answer = []
while A:
    I = [i for i,x in enumerate(A) if i + 1 == x]
    i = I[-1]
    answer.append(i + 1)
    A = A[:i] + A[i+1:]

answer = answer[::-1]
print('\n'.join(map(str,answer)))