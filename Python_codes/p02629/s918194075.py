def f(n):
    if n == 0:
        return ""
    n-=1
    return f(n//26) + chr(97 + n%26)

n = int(input())
print(f(n))