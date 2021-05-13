def main(N):
    if N==1:
        return 0
    elif N==2:
        return 2
    else:
        return (10**N - (9**N*2 - 8**N))%(10**9 + 7)

if __name__ == '__main__':
    N = int(input())
    ans = main(N)
    print(ans)

