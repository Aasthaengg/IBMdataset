def main():
    n, m = map(int, input().split())
    ans_dict = dict() # {問題i : [ACしたかどうか、ACに関係なく累計WA数]}

    for _ in range(m):
        p, s = input().split()

        if p not in ans_dict: # 初見の場合
            if s == "AC": # 正解
                ans_dict[p] = [1, 0]
            else: # 不正解
                ans_dict[p] = [0, 1]
        else: # 初見じゃない場合
            if ans_dict[p][0] == 1: # 正解済み
                continue
            else: # 未正解
                if s == "AC":
                    ans_dict[p][0] = 1
                else:
                    ans_dict[p][1] += 1

    ac_count = 0
    wa_count = 0
    for item in ans_dict.items():
        if item[1][0] == 1: # 正解済み
            ac_count += 1
            wa_count += item[1][1]

    print(ac_count, wa_count)


if __name__ == "__main__":
    main()
