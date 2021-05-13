import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10 ** 7)

def answer_is_X(X):
    mod = deque(sorted([i%X for i in A if i%X != 0]))
    answer = 0
    while mod:
        Amin = mod.popleft()
        answer += Amin
        while Amin > 0:
            # ポップできない場合
            if not mod:
                return False
            Amax = mod.pop()
            sub = X - Amax
            if sub <= Amin:
                Amin -= sub
            else:
                Amax += Amin
                mod.append(Amax)
                Amin = 0

    if answer <= K:
        return True
    else:
        return False

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

N,K = map(int,input().split())
A = [int(i) for i in input().split()]

sumA_divisors = make_divisors(sum(A))

answer = 0
for i in sumA_divisors:
    if answer_is_X(i):
        answer = i

print(answer)