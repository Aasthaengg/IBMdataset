import sys

N, A, B = map(int, sys.stdin.buffer.read().split())

# print(f'{N=} {A=} {B=}')
div, mod = divmod(N, A + B)
# print(f'{div=} {mod=}')
ans = div * A + min(mod, A)
print(ans)
