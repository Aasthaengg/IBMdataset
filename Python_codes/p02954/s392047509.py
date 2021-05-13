import re


S = input()
T = S.replace("RL", "$$")
devided_S = re.findall("R+L+", S)
ans = [-1 if T[i] == "$" else 0 for i in range(len(S))]

more_than_0 = []
for block in devided_S:
    count = len(block)
    r = block.count("R")
    l = count - r
    
    if count % 2 == 0:
        for _ in range(2):
            more_than_0.append(count//2)
    else:
        count_r = count//2 + (r > l)
        count_l = count - count_r
        more_than_0.append(count_r)
        more_than_0.append(count_l)
        if max(r, l) % 2 == 0:
            more_than_0[-1], more_than_0[-2] = more_than_0[-2], more_than_0[-1]

more_than_0.reverse()
for n in ans:
    if n == -1:
        print(more_than_0.pop(), end=" ")
    else:
        print(n, end=" ")
print()
