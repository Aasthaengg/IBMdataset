import sys
input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    S = input().rstrip()
    ac_freq = [0]
    for i in range(0, N-1):
        if S[i:i+2] == 'AC':
            ac_freq.append(ac_freq[-1] + 1)
        else:
            ac_freq.append(ac_freq[-1])
    ac_freq.append(ac_freq[-1])
    for _ in range(Q):
        l, r = map(int, input().split())
        print(ac_freq[r-1] - ac_freq[l-1])


if __name__ == '__main__':
    main()
