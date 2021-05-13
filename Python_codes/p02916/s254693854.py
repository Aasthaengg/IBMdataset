n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

ans = sum(b)
pre_idx = -1
pre_val = -1
for idx, val in enumerate(a):
    if pre_idx == -1:
        pre_idx = idx
        pre_val = val
    else:              # pre_idx != -1:
        if pre_val == val  - 1:
            ans = ans + c[pre_val - 1]
            pre_idx = idx
            pre_val = val
        else:
            pre_idx = idx
            pre_val = val   
        
print(ans)