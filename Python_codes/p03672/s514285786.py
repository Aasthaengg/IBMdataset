def main():
    S = input()
    N = len(S)
    for i in range(1,N//2):
        if S[:N//2-i] == S[N//2-i:N-i*2] :
            print(N-i*2)
            return
main()