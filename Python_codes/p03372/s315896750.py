n, c = [int(i) for i in input().split(" ")]
x = [0] * (n + 1)
v = [0] * (n + 1)

for i in range(1, n + 1):
    x[i], v[i] = [int(i) for i in input().split(" ")]

def s(x, v):
    #print(x, v)
    sum_v = [0] * (n + 1)
    for i in range(1, n + 1):
        sum_v[i] = sum_v[i - 1] + v[i]
    v_sub = [sum_v[i] - x[i] for i in range(0, n + 1)]
    max_v = [0] * (n + 1)
    for i in range(1, n + 1):
        max_v[i] = max(max_v[i - 1], v_sub[i])
    #print(max_v)
    
    sum_r = v[n]
    max_v_sub = max_v[n]
    for i in range(1, n // 2 + 1):
        v_sub = sum_r - (c - x[n - i + 1]) * 2 + max_v[n - i]
        #print(v_sub, i)
        if v_sub > max_v_sub:
            max_v_sub = v_sub
        sum_r += v[n - i]
    return max_v_sub
        
print(max(s(x, v), s([0] + [c - xi for xi in x[1::]][::-1], [0] + v[1::][::-1])))