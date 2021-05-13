import sys

readline = sys.stdin.readline
readlines = sys.stdin.readlines
ns = lambda: readline().rstrip() # input string
ni = lambda: int(readline().rstrip()) # input int
nm = lambda: map(int, readline().split()) # input multiple int 
nl = lambda: list(map(int, readline().split())) # input multiple int to list

n, k = nm()
values = nl()
a = 0
b = 0

for i, v in enumerate(values):
    tmp_a = 0
    cnt_b = 0
    for j, v_c in enumerate(values):
        if v > v_c:
            tmp_a += 1
            if i > j:
                cnt_b += 1
    tmp_b = tmp_a * k - cnt_b
    a -= tmp_a
    b += tmp_b
    
print((a * k * (k + 1) // 2 + (b - a) * k) % (10 ** 9 + 7))
    
