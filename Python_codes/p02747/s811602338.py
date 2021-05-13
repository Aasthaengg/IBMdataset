# H, W = [int(_) for _ in input().split()]
import sys
S = input()
if len(S) % 2 == 0:
    hi_list = []
    for i in range(0, len(S), 2):
        hi_list.append(S[i:i+2])
    if set(hi_list) == {'hi'}:
        print('Yes')
        sys.exit(0)
print('No')
