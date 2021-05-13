from collections import defaultdict

def main():
    N = int(input())
    MARCH = ['M','A','R','C','H']
    S = [0] * len(MARCH)
    for _ in range(N):
        s = input()
        if not s[0] in MARCH:
            continue
        if s[0] == MARCH[0]: S[0] += 1
        elif s[0] == MARCH[1]: S[1] += 1
        elif s[0] == MARCH[2]: S[2] += 1
        elif s[0] == MARCH[3]: S[3] += 1
        elif s[0] == MARCH[4]: S[4] += 1
    cnt = 0
    for i in range(len(S)-2):
        for j in range(i+1,len(S)-1):
            for k in range(j+1,len(S)):
                cnt += S[i]*S[j]*S[k]
    print(cnt)

if __name__ == '__main__':
    main()