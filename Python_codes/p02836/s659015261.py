import math

def main():
    S = input().rstrip()
    ans = 0
    for i in range(math.ceil(len(S) / 2)):
        if S[i] != S[-(i+1)]:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
