def main():
    N, D = map(int, input().split())
    dif = (D * 2) + 1
    if N % dif > 0:
        print((N // dif) + 1)
    else:
        print(N // dif) 
main()  