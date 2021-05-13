class common_function():
    """
        1. よく使いそうで予め用意しておいた変数をまとめた
        2. よく使いそうな関数群をまとめた
    """
    def __init__(self):
        """
            1. 英字の一覧をリストに格納しておいた変数
        """
        self.sletter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.bletter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def main():
    common = common_function()
    s = list(input())
    K = int(input())
    t = [0]
    for i in range(len(common.sletter)-1, 0, -1):
        t.append(i)

    u = []
    for i in range(len(s)):
        u.append(t[common.sletter.index(s[i])])
    
    ans = ''
    for i in range(len(s)-1):
        if u[i] <= K:
            ans += 'a'
            K -= u[i]
        else:
            ans += s[i]
    K = K%26
    if u[len(s)-1] <= K:
        K -= u[len(s)-1]
        ans += common.sletter[K]
    else:
        ans += common.sletter[common.sletter.index(s[len(s)-1])+K]
    print(ans)


if __name__ == "__main__":
    main()
