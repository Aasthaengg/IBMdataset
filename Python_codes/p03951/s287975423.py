def main():
    N = int(input())
    s = input()
    t = input()

    for i in range(N):
        if s[i:] == t[:N-i]:
            print(2*N-(N-i))
            return
    print(N*2)

main()