n = int(input())

def sss(s):
    return sum(map(int, list(str(s))))

ans = 10**7
for a in range(1, n):
    b = n-a
    ans = min(ans, sss(a)+sss(b))
print(ans)