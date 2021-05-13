import itertools
import sys
input = sys.stdin.readline

S = input().rstrip('\n')
N = len(S)

print(2*min(S.count('0'), S.count('1')))

# for i in itertools.count():
#     # print(S)
#     S = S.replace('01', '').replace('10', '')
#     if not S:
#         break
#     if S.count('0') == 0 or S.count('1') == 0:
#         break

# print(N-len(S))
