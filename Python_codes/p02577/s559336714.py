def main(N):
    ans = 0
    for n in str(N):
        ans += int(n)
    if ans%9==0:
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    N = int(input())
    ans = main(N)
    print(ans)

