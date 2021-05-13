mod = 10 ** 9 + 7
mod2 = 2**61+1
from collections import deque
import heapq
from bisect import bisect_left, insort_left

def iip(listed):
    ret = [int(i) for i in input().split()]
    if len(ret) == 1 and not listed:
        return ret[0]
    return ret


def main():
    r = solve()
    #print(r)

def solve():
    K = iip(False)
    S = input()
    S = [ord(i) for i in S]
    Q = iip(False)

    posit = {}
    for i in range(ord("a"), ord("z")+1):
        posit[i] = []

    query = []
    for i in range(Q):
        query.append(input().split())

    for i, j in enumerate(S, 1):
        posit[j].append(i)

    result = []
    for d in range(ord("a"), ord("z")+1):
        #print(chr(d), posit[d])
        pass


    for q in query:
        if q[0] == "1":
            p = int(q[1])
            before = S[p-1]
            after = ord(q[2])
            if before == after:
                continue
            S[p-1] = after

            idx = bisect_left(posit[before], p)

            posit[before].pop(idx)
            insort_left(posit[after], p)

        else:
            l = int(q[1])
            r = int(q[2])

            ret = 0
            for i in range(ord("a"), ord("z")+1):
                ll = bisect_left(posit[i], l)

                if not posit[i]:  # 文字が存在しなければcontinue
                    #print("e2")
                    continue
                if l > posit[i][-1]:  # lより小さい文字しかなければcontinue
                    continue
                if posit[i][ll] > r:  # l以上のpositionで一番小さいものがrより大きければcontinue
                    #print("e3")
                    continue

                    #print(chr(i))
                ret += 1  # いずれのcontinue条件にも引っかからなければスコアを１増やす
            result.append(ret)


    #print(S)
    #print(posit)
    split_print_space(result)

    return



#####################################################ライブラリ集ここから

def split_print_space(s):
    print(" ".join([str(i) for i in s]))


def split_print_enter(s):
    print("\n".join([str(i) for i in s]))


def koenai_saidai_x_index(sorted_list, n):
    l = 0
    r = len(sorted_list)
    if len(sorted_list) == 0:
        return False
    if sorted_list[0] > n:
        return False

    while r - l > 1:
        x = (l + r) // 2
        if sorted_list[x] == n:
            return x
        elif sorted_list[x] > n:
            r = x
        else:
            l = x
    return l


def searchsorted(sorted_list, n, side):
    if side not in ["right", "left"]:
        raise Exception("sideはrightかleftで指定してください")

    l = 0
    r = len(sorted_list)

    if n > sorted_list[-1]:
        # print(sorted_list)
        return len(sorted_list)
    if n < sorted_list[0]:
        return 0

    while r - l > 1:
        x = (l + r) // 2
        if sorted_list[x] > n:
            r = x
        elif sorted_list[x] < n:
            l = x
        else:
            if side == "left":
                r = x
            elif side == "right":
                l = x

    if side == "left":
        if sorted_list[l] == n:
            return r - 1
        else:
            return r

    if side == "right":
        if sorted_list[l] == n:
            return l + 1
        else:
            return l


def soinsuu_bunkai(n):
    ret = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            n //= i
            ret.append(i)
        if i > n:
            break
    if n != 1:
        ret.append(n)
    return ret


def conbination(n, r, mod, test=False):
    if n <= 0:
        return 0
    if r == 0:
        return 1
    if r < 0:
        return 0
    if r == 1:
        return n
    ret = 1
    for i in range(n - r + 1, n + 1):
        ret *= i
        ret = ret % mod

    bunbo = 1
    for i in range(1, r + 1):
        bunbo *= i
        bunbo = bunbo % mod

    ret = (ret * inv(bunbo, mod)) % mod
    if test:
        # print(f"{n}C{r} = {ret}")
        pass
    return ret


def inv(n, mod):
    return power(n, mod - 2)


def power(n, p, mod_= mod):
    if p == 0:
        return 1
    if p % 2 == 0:
        return (power(n, p // 2, mod_) ** 2) % mod_
    if p % 2 == 1:
        return (n * power(n, p - 1, mod_)) % mod_


if __name__ == "__main__":
    main()