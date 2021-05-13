import sys
input = sys.stdin.readline


def main():
    S = input().strip()
    r_cnt = 0
    l_cnt = 0
    flag = True  # counting "R"
    for idx, s in enumerate(S):
        if flag and s == "R":
            r_cnt += 1
        elif flag and s == "L":
            flag = False
            l_cnt += 1
        elif not flag and s == "L":
            l_cnt += 1
        elif not flag and s == "R":
            if r_cnt > 1:
                print(" ".join(["0"] * (r_cnt - 1)), end=" ")
            print((r_cnt // 2) + (r_cnt % 2) + l_cnt // 2, r_cnt // 2 + (l_cnt // 2) + l_cnt % 2, end=" ")
            if l_cnt > 1:
                print(" ".join(["0"] * (l_cnt - 1)), end=" ")
            l_cnt = 0
            r_cnt = 1
            flag = True

    if r_cnt > 1:
        print(" ".join(["0"] * (r_cnt - 1)), end=" ")
    print((r_cnt // 2) + (r_cnt % 2) + l_cnt // 2, r_cnt // 2 + (l_cnt // 2) + l_cnt % 2, end=" ")
    if l_cnt > 1:
        print(" ".join(["0"] * (l_cnt - 1)), end=" ")
    print()


if __name__ == "__main__":
    main()
