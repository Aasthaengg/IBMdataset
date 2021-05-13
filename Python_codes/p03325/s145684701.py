# C - *3 or /2

N = int(input())
A = list(int(a) for a in input().split())

def devide2(x):
    if x%2:
        return 0
    else:
        ret = 0
        while True:
            ret += 1
            x //= 2
            if x%2:
                return ret

ans = 0
for a in A:
    ans += devide2(a)
    
print(ans)