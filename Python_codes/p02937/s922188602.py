from bisect import bisect_left
from string import ascii_lowercase


def main():
    s = input()
    t = input()

    set_s = set(tuple(s))
    set_t = set(tuple(t))

    if not(set_t <= set_s):
        print(-1)
        exit()

    ans = 0
    d = {c:[] for c in ascii_lowercase}
    
    for i, c in enumerate(s):
        d[c].append(i+1)
    
    now = 0
    for c in t:
        
        idx = bisect_left(d[c], now+1)

        if idx == len(d[c]):
            ans += len(s)
            now = 0
            idx = bisect_left(d[c], now+1)
            
        now = d[c][idx]

    ans += now
    print(ans)

        
if __name__ == "__main__":
    main()