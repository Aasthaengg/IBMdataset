import sys,math,collections,itertools
input = sys.stdin.readline

s = input().rstrip()[::-1]
DP=[0 for _ in range(13)]

DP[0]=1
m = 10**9+7
mul = 1
for i in range(len(s)):
    dig = s[i]
    nextDP = [0 for _ in range(13)]
    if dig == '?':
        for j in range(10):
            for k in range(13):
                nextDP[(k+mul*j)%13] += DP[k]
                nextDP[(k+mul*j)%13]%=m
    else:
        j = int(dig)
        for k in range(13):
            nextDP[(k+mul*j)%13] += DP[k]
            nextDP[(k+mul*j)%13]%=m

    mul *= 10
    mul%=13
    DP = nextDP

print(DP[5]%m)
        
