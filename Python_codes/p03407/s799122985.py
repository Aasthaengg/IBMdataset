def main(a,b,c):
    return c <= a+b

a,b,c = map(int, input().split())
print("Yes" if main(a,b,c) else "No")