import collections
import string

def solve(s):
    s = s.lower()
    counter = collections.Counter(s)
    lows = string.ascii_lowercase
    cnt = [counter[ch] for ch in lows]
    for (ch, n) in zip(lows, cnt):
        print('{0} : {1}'.format(ch, n))

if __name__ == '__main__':
    s = ''
    while True:
        try:
            s += input()
        except:
            break
    solve(s)