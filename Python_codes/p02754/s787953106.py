"""
A = 3, B = 4
[青青青][赤赤赤赤][青青青][赤赤赤]...

N = 8
[青青青赤赤赤赤青]

return 青 = 4
"""

def count_balls():
    # 入力
    N, A, B = map(int, input().split())
    # [青青青赤赤赤赤]の個数と余り
    comb_count = N // (A + B)
    remainder = N % (A + B)
    # 集計
    if remainder <= A:
        return A * comb_count + remainder
    else:
        return A * comb_count + A

result = count_balls()
print(result)