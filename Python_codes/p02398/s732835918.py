a,b,c = map(int, raw_input().split())
ret = []
for i in range(a, b+1, 1):
    if c % i == 0:
        ret += [i]
print(len(ret))