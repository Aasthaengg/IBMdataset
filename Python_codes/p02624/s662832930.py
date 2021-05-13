import sys
def input():
    return sys.stdin.readline().rstrip('\n')
    

def calc(N):
    ans = 0
    for i in range(1, N + 1):
        k = N // i
        ans += i * k * (k + 1) // 2
    return ans



N = int(input())
print(calc(N))