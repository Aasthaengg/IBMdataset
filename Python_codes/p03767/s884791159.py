def main():
    N=int(input())
    a=sorted([int(_) for _ in input().split()])[::-1]
    print(sum(a[1:2*N+1:2]))
main()
