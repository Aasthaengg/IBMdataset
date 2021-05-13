def solve(a, b):
    if b < a:
        a, b = b, a
    print(a, b)

if __name__ == '__main__':
    while True:
        a, b = [int(i) for i in input().split()]
        if a == 0 and b == 0: break
        solve(a, b)