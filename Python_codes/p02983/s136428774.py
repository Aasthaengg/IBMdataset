
url = "https://atcoder.jp//contests/abc133/tasks/abc133_c"

def main():
    t = list(map(int, input().split()))
    ans = []
    for i in range(t[0], t[1]+1):
        for j in range(i+1, t[1]+1):
            val = (i*j) % 2019
            if val == 0:
                print(val)
                exit()
            ans.append(val)
    print(min(ans))


if __name__ == '__main__':
    main()