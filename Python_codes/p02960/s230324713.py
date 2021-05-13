import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from copy import copy 
def main():
    S = readline().decode().rstrip()
    P = int(1e9)+7
    DP = [0 for _ in range(13)]
    DP[0] = 1
    mul = 0
    for k in reversed(S):
        nxDP = [0 for _ in range(13)]
        if k == '?':
            for j in range(10):
                r = (j*pow(10, mul, 13))%13
                for i in range(13):
                    nxDP[(r+i)%13] += DP[i] 
                    nxDP[(r+i)%13] %= P  
        else:
            r = ((ord(k)-ord('0'))*pow(10, mul, 13))%13
            for i in range(13):
                nxDP[(r+i)%13] += DP[i] 
                nxDP[(r+i)%13] %= P
        mul += 1
        DP = copy(nxDP)
    print(DP[5])
if __name__ == '__main__':
    main()