n = int(input())
A = list(map(int, input().split()))

def f(a, ans):
    for i in range(1,n):
        b = A[i]            
        if a> 0:
            if a + b >= 0:
                ans += abs(-1-a-b)
                a = -1
            else:
                a += b
        elif a < 0:
            if a+b <= 0:
                ans += abs(1-a-b)
                a = 1
            else:
                a += b
    return ans

# A[0] の初期符号が正しいと仮定してしまっているが、そうとは限らない。
a = A[0]
q = 10**15
if a > 0:
    q = min(f(a,0), f(-1,a+1))
elif a < 0:
    q = min(f(a,0),f(1,-a+1))
else:
    q = min(f(1,1),f(-1,1))

print(q)