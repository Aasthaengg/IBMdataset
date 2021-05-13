import sys
from collections import defaultdict
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    V = list(map(int, input().split()))

    d_odd = defaultdict(int)
    d_even = defaultdict(int)
    one_kind = True
    for i, v in enumerate(V):
        if v != V[0]: one_kind = False
        if i % 2 == 0: d_even[v] += 1
        if i % 2 != 0: d_odd[v] += 1
    if one_kind:
        print(n // 2)
        return
    
    """
    修正した結果すべての数字が一致する場合を省かないといけないのがコーナーケース
    """
    
    even_list = list(d_even.values())
    even_list.sort()
    even_max = even_list.pop()
    even_pre_max = even_list.pop() if len(even_list) > 0 else -10**10
    odd_list = list(d_odd.values())
    odd_list.sort()
    odd_max = odd_list.pop()
    odd_pre_max = odd_list.pop() if len(odd_list) > 0 else -10**10

    even_max_key = [k for k, v in d_even.items() if v == even_max]
    odd_max_key = [k for k, v in d_odd.items() if v == odd_max]
   

    if len(even_max_key) == 1 and len(odd_max_key) == 1 and even_max_key[0] == odd_max_key[0]:
        print(min(n - even_max - odd_pre_max, n - even_pre_max - odd_max))
    else:
        print(n - even_max - odd_max)

if __name__ == "__main__":
    main()
