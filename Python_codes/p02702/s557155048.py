from collections import Counter

def solve_baka(s: str):
    ans = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if int(s[i:j]) % 2019 == 0:
                print(i, j)
                ans += 1

    return ans


def main():
    s = input()
    sr = s[::-1]
    tn = [0]

    m = 1
    for i in range(len(s)):
        tn.append((tn[i]+int(sr[i])*m) % 2019)
        m = m * 10 % 2019

    ans = 0
    for _, v in Counter(tn).items():
        if v > 1:
            ans += v * (v - 1) // 2
    print(ans)


if __name__ == '__main__':
    main()
