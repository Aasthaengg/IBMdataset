# coding: utf-8

# https://atcoder.jp/contests/abc097/tasks/arc097_a
# 0:37-0:50 chudan
# 12:14-12:20
# 12:30-
# 14:40-14:53


def main():
    S = input()
    N = len(S)
    K = int(input())

    def rec(tree, substr):
        if len(substr) > 0:
            ans.append(substr)

        if len(ans) == K:
            return None

        keys = sorted(tree.keys())
        for key in keys:
            rec(tree[key], substr+key)
    
    min_char_list = sorted(list(set(S)))

    ans = []
    for min_char in min_char_list:
        if len(ans) >= K:
            break

        min_char_i = []
        for i, s in enumerate(S):
            if s == min_char:
                min_char_i.append(i)

        substrs = []
        for i in min_char_i:
            substrs.append(S[i:min(i+(K-len(ans)), N)])

        prefix_tree = {}
        for substr in substrs:
            tree = prefix_tree
            for c in substr:
                if c not in tree:
                    tree[c] = {}
                tree = tree[c]

        # prefix tree starting the minimum letter: created

        rec(prefix_tree, "")

    return ans[K-1]


print(main())
