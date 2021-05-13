a, b = map(int, input().split())

res_c = 16 - min(a, b)*2
res_ab = max(a, b) - min(a, b)
if 2*res_ab > res_c:
    print(':(')
elif 2*res_ab <= res_c:
    print('Yay!')