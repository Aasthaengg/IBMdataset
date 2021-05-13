A, B = map(int, input().split())

def ReverseDigits(n):
    d = str()
    for i in range(5):
        d += str(n % 10)
        n = n // 10
    return(d)

ans = 0

for i in range(A, B+1):
    if str(i) == ReverseDigits(i):
        ans += 1
    else:
        pass

print(ans)