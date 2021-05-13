def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    # cs = sum(a[:i]) % m
    cs = 0
    # dic[i] = len({j | sum[:j] % m == i})
    dic = {0:1}

    ans = 0
    for i, x in enumerate(a):
        cs += x
        cs %= m
        if cs in dic:
            ans += dic[cs]
            dic[cs] += 1
        else:
            dic[cs] = 1
    
    print(ans)

main()