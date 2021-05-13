import math

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    a = min([A,B,C,D,E])
    ans = math.ceil(N/a) + 4
    print(ans)

if __name__ == '__main__':
    main()