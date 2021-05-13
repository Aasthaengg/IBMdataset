def main():
    N=int(input())
    A=[int(_) for _ in input().split()]
    tmp = 1
    for a in A:
        if a%2==0:
            tmp *= 2
    print(3**N-tmp)
main()