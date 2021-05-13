import sys
stdin = sys.stdin
 
ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split()))
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

N = ri()
A = [ri() for _ in range(N)]
even_cnt = sum([1 for x in A if x % 2 == 0])
odd_cnt = N - even_cnt
print('first' if odd_cnt else 'second')
