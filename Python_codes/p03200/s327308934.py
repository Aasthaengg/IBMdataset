# -*- coding: utf-8 -*-
def main():
    S = list(input())
    Bcnt = 0
    ans = 0
    for i in range(len(S)):
        if S[i] == 'B':
            Bcnt += 1
        else:
            ans += Bcnt
    print(ans)
if __name__ == '__main__':
    main()