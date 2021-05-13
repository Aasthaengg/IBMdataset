
def main():
    S = input()
    cnt = 0
    ans = 0
    f = 1
    for i in range(3):
        if S[i] == 'R':
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(ans)
    


if __name__ == "__main__":
    main()