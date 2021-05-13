def main():
    S = input()
    akiba = "kihbr".upper()+"?"
    a = [1, 0, 0, 1, 1, 1]

    ind = 0
    a_num = []
    cnt = 0
    for s in S:
        if s == "A":
            cnt += 1
            continue
        if s != akiba[ind]:
            return "NO"
        if s == akiba[ind]:
            ind += 1
            a_num.append(cnt)
            cnt = 0
    else:
        a_num.append(cnt)

    if len(a_num) < len(a):
        return "NO"
    for x, y in zip(a, a_num):
        if y > x:
            return "NO"

    return "YES"


if __name__ == "__main__":
    print(main())
