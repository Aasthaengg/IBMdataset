import sys
import numpy as np
input = sys.stdin.readline

def main():
    s = input().strip()

    count = np.zeros((len(s), ord("z") - ord("a") + 1), dtype=int)
    s_ = [0] * len(s)
    s_[0] = ord(s[0]) - ord("a")
    count[0][s_[0]] += 1
    for i in range(1, len(s)):
        s_[i] = ord(s[i]) - ord("a")
        count[i] += count[i-1]
        count[i][s_[i]] += 1
    
    ans = 0
    for i in range(len(s)-1):
        tmp = len(s) - i - 1 - (count[-1, s_[i]] - count[i, s_[i]])
        ans += tmp
    print(ans+1)

if __name__ == "__main__":
    main()