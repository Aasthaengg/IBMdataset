N = int(input())
if N < 10:
    print(N)
else:
    str_N = str(N)
    ### 最上位以外すべて9 の場合はその値が最大値
    for n in str_N[1:]:
        if n != '9':
            ### それ以外は最上位の桁を一つ下げてあと全部9 が一番最大
            print(int(str_N[0]) - 1 + (len(str_N) - 1) * 9)
            break
    else:
        print(int(str_N[0]) + (len(str_N) - 1) * 9)

