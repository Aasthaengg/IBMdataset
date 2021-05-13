a, b = map(int, input().split())
def solve():
    for i in range(1, 1010):
        if int(i*0.08) == a and int(i*0.1) == b:
            print(i)
            return
    print(-1)

solve()