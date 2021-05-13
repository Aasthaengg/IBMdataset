def main():
    N=int(input())
    K=int(input())
    x=[int(_) for _ in input().split()]
    print(sum([min(K-xi,xi) for xi in x])*2)

main()