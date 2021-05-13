def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

import sys

N, M = MI()
ans = ""
num = [[] for _ in range(N)]

for _ in range(M):
    s, c = MI()
    num[s - 1].append(str(c))

    if (N != 1 and (s, c) == (1, 0)) or len(set(num[s - 1])) != 1:
        print(-1)
        sys.exit()

if num[0] == []:
    ans += str(int(N != 1))
else:
    ans += num[0][0]

for n in num[1:]:
    if n == []:
        ans += "0"
        continue
        
    ans += n[0]

print(ans)