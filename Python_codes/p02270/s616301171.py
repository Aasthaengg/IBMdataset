import sys
def input():
    return sys.stdin.readline()[:-1]
    
n,k = map(int, input().split())
w = [int(input()) for i in range(n)]

def get_v(n,k,w,P):
    c = 0
    val = 0
    for i in w:
        val += i
        if val > P:
            c += 1
            val = i
            if c >= k:
                return 0
    return 1

left = max(w)
right = sum(w)
while True:
    P = (left + right)//2
    ret = get_v(n,k,w,P)
    if ret:
        right = P
    else:
        left = P + 1
    if left == right:
        break
print(left)
