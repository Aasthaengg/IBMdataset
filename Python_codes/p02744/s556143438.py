from copy import copy
n = int(input())
data = ["a"] * n
ans = ["".join(data)]

def print_str(ans, data, i):
    if i == n:
        return 
    ans.append("".join(data))
    mx = max(data[i] for i in range(n))
    while ord(data[i]) + 1 <= ord(mx) + 2:
        s = copy(data)
        ans.append("".join(data))
        print_str(ans, s, i + 1)
        data[i] = chr(ord(data[i]) + 1)
    data = ["a"] * n
    print_str(ans, data, i + 1)

print_str(ans, data, 1)
ans = sorted(set(ans))
for i in range(len(ans)):
    print(ans[i])