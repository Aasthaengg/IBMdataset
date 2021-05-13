N=int(input())

from collections import defaultdict
import itertools
def soinsu(n):
    arr = []
    now = n
    for i in range(2, int(n**0.5)+1):
        if now%i==0:
            cnt=0
            while now%i==0:
                cnt+=1
                now //= i
            arr.append([i, cnt])
    if now!=1:
        arr.append([now, 1])
#     if arr==[]:
#         arr.append([n, 1])
    return arr

d = defaultdict(int)
for i in range(1,N+1):
    bunkai =soinsu(i)
    for b in bunkai:
        d[b[0]]+=b[1]

prime_list=[k for k in d.keys() if d[k]>=2]

N2 = sum(d[k]>=2 for k in d.keys())
N4 = sum(d[k]>=4 for k in d.keys())

N14 = sum(d[k]>=14 for k in d.keys())
N24 = sum(d[k]>=24 for k in d.keys())
N74 = sum(d[k]>=74 for k in d.keys())

pattern2_4_4 = N4*(N4-1)*(N2-2)//2
pattern2_24 = N24*(N2-1)
pattern4_14 = N14*(N4-1)
pattern74 = N74

print(pattern2_4_4 + pattern2_24 + pattern4_14+pattern74)