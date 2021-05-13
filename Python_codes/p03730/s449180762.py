a, b, c = list(map(int, input().split()))

def main():
    for x in range(a, b*a+1, a):
        if x%b == c:
            print('YES')
            return
    print('NO')
    return
main()