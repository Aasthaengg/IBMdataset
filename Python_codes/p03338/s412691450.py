import string

N = int(input())
S = input()

result = 0
for i in range(1, N+1):
    S_forward = S[:i]
    S_backward = S[i:]
    is_same = 0
    for j in string.ascii_lowercase:
        if j in S_forward and j in S_backward:
            is_same += 1
    result = max(result, is_same)

print(result)