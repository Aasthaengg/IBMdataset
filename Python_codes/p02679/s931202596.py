from collections import defaultdict

def gcd(x, y):
    r = x % y
    while r:
        x, y, r = y, r, y%r
    return y
    
def main():
    n = int(input())
    mod = 1000000007
    p = defaultdict(lambda: 0)
    bad = dict()
    zeros = 0
    for _ in range(n):
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            zeros += 1
        else:
            if a == 0:
                p["0"] += 1
                bad["0"] = "INF"
            elif b == 0:
                p["INF"] += 1
                bad["INF"] = "0"
            else:
                g = gcd(b, a)
                a //= g
                b //= g
                sp = f"{a}_{b}"
                if b < 0:
                    b *= -1
                    a *= -1
                sm = f"{b}_{-a}"
                p[sp] += 1
                bad[sp] = sm
    done = set()
    good = 0
    ans = 1
    for key, num in p.items():
        if key in done:
            continue
        b = p.get(bad[key])
        done.add(bad[key])
        if b:
            ans *= pow(2, b, mod)+pow(2, num, mod)-1
            ans %= mod
        else:
            good += num
    ans *= pow(2, good, mod)
    ans += zeros
    ans -= 1
    ans %= mod
    print(ans)
        
        

if __name__ == "__main__":
    main()