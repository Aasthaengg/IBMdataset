def is_ok(gen, res):
    if res == "Vacant":
        exit()
    return gen == res


def meguru_bisect_kai(ng, ok, gen):
    while True:
        mid = (ng + ok) // 2
        print(mid, flush=True)
        res = input()

        if is_ok(gen, res):
            if (mid - ng) % 2:
                ok = mid
            else:
                ng = mid
        else:
            if (mid - ng) % 2:
                ng = mid
                gen = res
            else:
                ok = mid


n = int(input())

print(0, flush=True)
res = input()
if res == "Vacant":
    exit()

ng = 0
ok = n
gen = res

meguru_bisect_kai(ng, ok, gen)