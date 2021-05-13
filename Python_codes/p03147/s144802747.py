import sys
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 10 ** 9 + 7

n = I()
hl = LI()
wl = []
count = 0

len_h = len(hl)

def m1(n):
    if n > 0:
        n = n - 1
    else:
        n = 0
    return n

max_hana = max(hl)
if max_hana == 0:
    print(0)
    sys.exit()

for i in range(max_hana):
    for j in range(len_h):
        if j == 0:
            if hl[j] > 0:
                count += 1
        else:
            if hl[j] > 0 and hl[j-1] == 0:
                count += 1
            elif hl[j] > 0 and hl[j-1] == 0:
                count += 1
    hl = list(map(m1, hl))

print(count)