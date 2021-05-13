N, K = map(int, input().split())

bit0_count = [0] * 64
bit1_count = [0] * 64

for A in map(int, input().split()):
    for i in range(64):
        if A & (1 << i):
            bit1_count[i] += 1
        else:
            bit0_count[i] += 1

ans = 0
less = -1
equal = 0
for i in range(63, -1, -1):
    if K & (1 << i):
        if less == -1:
            less = bit1_count[i] * (1 << i)
        else:
            less += max(bit0_count[i], bit1_count[i]) * (1 << i)
    
        if bit0_count[i] > bit1_count[i]:
            equal += bit0_count[i] * (1 << i)
        else:
            equal += bit1_count[i] * (1 << i)
            less = max(less, equal)
    else:
        equal += bit1_count[i] * (1 << i)
        if less != -1:
            less += max(bit0_count[i], bit1_count[i]) * (1 << i)
    
print(max(less, equal))