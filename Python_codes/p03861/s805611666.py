a, b, x = map(int, input().split())

def count(n, x):
    if n < 0:
        return 0
    else:
        return n//x+1
ans = count(b, x)-count(a-1, x)
print(ans)
