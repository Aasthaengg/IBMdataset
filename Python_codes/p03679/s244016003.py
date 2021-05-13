
def main():
    t = list(map(int, input().split()))
    ans = ''
    if t[1] >= t[2]:
        ans = 'delicious'
    elif t[0] >= t[2] - t[1]:
        ans = 'safe'
    if t[0] < t[2] - t[1]:
        ans = 'dangerous'
    print(ans)

if __name__ == '__main__':
    main()
