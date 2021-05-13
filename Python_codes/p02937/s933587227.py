from bisect import bisect_right

def main():
    S = input()
    T = input()
    lens = len(S)
    s = set(S)
    t = set(T)
    for i in t:
        if not i in s:
            return -2
    S = S + S
    alpha = [[] for i in range(26)]
    for i, v in enumerate(S):
        alpha[ord(v)-ord('a')].append(i)
    ans = 0
    idx = -1
    cnt = 0
    for i in T:
        # 二分探索で探す
        idx = bisect_right(alpha[ord(i)-ord('a')], idx)
        idx = alpha[ord(i)-ord('a')][idx]
        cnt += idx // lens
        idx %= lens
        ans = cnt * lens + idx
    return ans

print(main()+1)
