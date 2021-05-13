def solve():
    # 標準入力部分
    N = int(input())  # len(person)
    A = []
    x = []
    y = []
    i = 0
    for i in range(N):
        A.append(int(input()))
        x.append([])
        y.append([])
        for j in range(A[i]):
            x_temp, y_temp = list(map(int, input().split()))
            x[i].append(x_temp)
            y[i].append(y_temp)
    
    # N人を正直者，不親切な人と仮定して矛盾せずに存在しうる正直者の最大人数を求める．
    honest_num = 0
    honest_num_new = 0
    for b in range(2**N):
        consistent = True
        case = format(b, '0'+str(N)+'b')
        # 矛盾があるか確認する処理, n-bit目が'1'のとき，n番目の人は正直者
        i = 0
        for i in range(N): # i番目の人の証言を検証
            for z in zip(x[i], y[i]): #z[0]（person[i]）がz[1]（正直者，不親切な人）であるという証言
                if case[i] == "1":
                    if case[z[0]-1] != str(z[1]):
                        consistent = False
        if consistent:
            # 矛盾がないとき，正直者の数を求める処理
            honest_num_new = case.count("1")
        # これまでの最大の人数と比較して，正直者が多いほうを採用
        honest_num = max(honest_num, honest_num_new)
    print(honest_num)



if __name__ == "__main__":
    solve()
