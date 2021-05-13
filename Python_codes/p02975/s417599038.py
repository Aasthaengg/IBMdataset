import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

"""
・a,b,a+b,a,b,a+b,...
・0,a,a,0,a,a,...
・0,0,0,0,0,0,...
"""

N,*A = map(int,read().split())

def solve(N,A):
    if all(x == 0 for x in A):
        return True
    q,r = divmod(N,3)
    if r:
        return False
    from collections import Counter
    counter = Counter(A)
    n = len(counter)
    if n == 1:
        return False
    if n == 2:
        a,b = counter.keys()
        if a > b:
            a,b = b,a
        if a != 0:
            return False
        # 0,b
        if counter[0] != N//3:
            return False
        return True
    if n == 3:
        a,b,c = counter.keys()
        for x in [a,b,c]:
            if counter[x] != q:
                return False
        return a^b^c == 0

answer = 'Yes' if solve(N,A) else 'No'
print(answer)