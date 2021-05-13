MOD = 10**9 + 7

def main():
    n, k = map(int, input().split())# 正0でコーナー
    a = list(map(int, input().split()))
    pos = []
    neg = []
    zero = []
    for v in a:
        if v == 0:
            zero.append(v)
        elif 0 < v:
            pos.append(v)
        else:
            neg.append(v)
    if len(pos) + len(neg) < k:
        print(0)
    else:
        if k%2 == 0:
            if len(pos) + len(neg) == k and len(pos) % 2 == 1:#負になる
                if len(zero) > 0:
                    print(0)
                else:
                    ans = 1
                    for v in pos:
                        ans *= v
                        ans %= MOD
                    for v in neg:
                        ans *= v
                        ans %= MOD
                    print(ans % MOD)
            else:
                pos.sort(reverse=True)
                neg.sort()
                ans = 1
                p, q = 0, 0
                while k > 0:
                    if p+1 < len(pos) and q+1 < len(neg):
                        x, y = pos[p]*pos[p+1], neg[q]*neg[q+1]
                        if x > y:
                            ans *= x
                            p += 2
                        else:
                            ans *= y
                            q += 2
                    elif p+1 < len(pos):
                        ans *= pos[p]*pos[p+1]
                        p += 2
                    else:
                        ans *= neg[q]*neg[q+1]
                        q += 2
                    k -= 2
                    ans %= MOD
                print(ans % MOD)
        else:
            if 0 == len(pos):
                if 0 < len(zero):
                    print(0)
                else:
                    neg.sort(reverse=True)
                    ans = 1
                    for i in range(k):
                        ans *= neg[i]
                        ans %= MOD
                    print(ans)
            else:
                pos.sort(reverse=True)
                neg.sort()
                ans = pos[0]
                p, q = 1, 0
                k -= 1
                while k > 0:
                    if p+1 < len(pos) and q+1 < len(neg):
                        x, y = pos[p]*pos[p+1], neg[q]*neg[q+1]
                        if x > y:
                            ans *= x
                            p += 2
                        else:
                            ans *= y
                            q += 2
                    elif p+1 < len(pos):
                        ans *= pos[p]*pos[p+1]
                        p += 2
                    else:
                        ans *= neg[q]*neg[q+1]
                        q += 2
                    k -= 2
                    ans %= MOD
                print(ans % MOD)

if __name__ == "__main__":
    main()
