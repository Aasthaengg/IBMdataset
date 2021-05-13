import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, P = mapint()
As = list(mapint())
bit = [a%2 for a in As]

pos = {}
pos[0] = 1
for i in range(1, N+1):
    pos[i] = pos[i-1]*i
dic = {}
dic[0] = 0
dic[1] = 0
for i in bit:
    dic[i] += 1

ans = 2**dic[0]
if P==1:
    if dic[1]<1:
        print(0)
        exit(0)
    else:
        pass
        # ans*=dic[1]
        # dic[1] -= 1
val = 0
for i in range(dic[1]//2+1):
    val += pos[dic[1]]//pos[i*2]//pos[dic[1]-i*2]
print(val*ans)