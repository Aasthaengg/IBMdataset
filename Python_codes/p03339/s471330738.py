import sys


if __name__ == "__main__":
    n = int(input())
    s = input()
    sum_w = s.count("W")
    sum_e = s.count("E")
    ans = 10**9
    w,e = 0,0
    for i in range(n):
        if s[i] == "W":
            sum_w-=1
        else:
            sum_e-=1
        chenge = w + sum_e
        if s[i] == "W":
            w += 1
        else:
            e += 1
        ans = min(ans,chenge)
    print(ans) 