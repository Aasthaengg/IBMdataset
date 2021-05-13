def main():
    N = int(input())
    S, T = map(str, input().split(' '))
    a = ''
    for i in range(N):
        a = a + S[i] + T[i]
    print(a)
main()