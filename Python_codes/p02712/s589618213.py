def solve():
    N = int(input())
    suma = 0
    for i in range(N+1):
        if i % 3 != 0 and i % 5 != 0:
            suma += i
    print(suma)

if __name__ == '__main__':
    solve()
