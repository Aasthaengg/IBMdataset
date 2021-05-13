# 符号の数について、-が偶数だった場合、全てを打ち消せる
# 奇数だった場合、どれか一つが残る。
# `..,+,-,+,..`を→移動←移動できるので

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ret = sum(abs(a) for a in A)
    num_neg = sum(a < 0 for a in A)
    min_abs_A = min(abs(a) for a in A)
    if num_neg % 2 == 1:
        ret -= 2*min_abs_A
        
    print(ret)
    
solve()