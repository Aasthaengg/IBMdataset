n = int(input())

print(0, flush=True)
s = input()
if s == 'Vacant':
    exit()
head_v = s
head_i = 0
print(n-1, flush=True)
s = input()
if s == 'Vacant':
    exit()
tail_v = s
tail_i = n-1

while True:
    mi = (head_i + tail_i) // 2
    print(mi, flush=True)
    mv = input()

    if mv == 'Vacant':
        exit()
    if tail_v == mv and (tail_i - mi) % 2 == 1 or tail_v != mv and (tail_i - mi) % 2 == 0:
        head_i = mi
        head_v = mv
    else:
        tail_i = mi
        tail_v = mv
