import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
from itertools import accumulate
from bisect import bisect_left

if N==0:
    print(0)
elif N>0:
    even = [0, 1]
    for i in range(1, 21):
        even.append(2**(i*2))
    cum = list(accumulate(even))
    idx = bisect_left(cum, N)
    maxi = cum[idx]-cum[idx-1]
    val = N-cum[idx-1]
    ans = ['1']
    up = maxi
    for i in range(maxi.bit_length()-1):
        up //= 2
        if val>up:
            if i%2==0:
                ans.append('0')
            else:
                ans.append('1')
            val -= up
        else:
            if i%2==0:
                ans.append('1')
            else:
                ans.append('0')
    print(''.join(ans))
elif N<0:
    N = -N
    even = [0]
    for i in range(21):
        even.append(2**(i*2+1))
    cum = list(accumulate(even))
    idx = bisect_left(cum, N)
    maxi = cum[idx]-cum[idx-1]
    val = N-cum[idx-1]
    ans = ['1']
    up = maxi
    for i in range(maxi.bit_length()-1):
        up //= 2
        if val>up:
            if i%2==0:
                ans.append('0')
            else:
                ans.append('1')
            val -= up
        else:
            if i%2==0:
                ans.append('1')
            else:
                ans.append('0')
    print(''.join(ans))