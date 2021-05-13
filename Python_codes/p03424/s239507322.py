n = int(input())
s = input().split()

s_t = set(s)
if len(s_t) == 3:
    print('Three')
elif len(s_t) == 4:
    print('Four')
