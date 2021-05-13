# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(S, T):
    d = dict()
    for i in range(len(S)):
        if S[i] != T[i]:
            if T[i] not in d:
                d[T[i]] = True
                S = ''.join([T[i] if s == S[i] else S[i] if s == T[i] else s for s in S])
            else:
                return False
    if S == T:
        return True
    return False

if __name__ == '__main__':
    input = sys.stdin.readline
    S = input().rstrip()
    T = input().rstrip()
    ans = main(S, T)
    print('Yes' if ans else 'No')
