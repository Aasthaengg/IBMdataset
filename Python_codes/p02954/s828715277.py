import sys
sys.setrecursionlimit(10**9)

def main():
    S = list(input())
    comp = []

    pre_s = S[0]
    length = 1
    for s in S[1:]:
        if s == pre_s:
            length += 1
        else:
            comp.append((pre_s,length))
            length = 1

        pre_s = s

    comp.append((pre_s,length))

    ans = []
    # print(comp)
    for i in range(len(comp)//2):
        ev = comp[i*2][1]
        od = comp[i*2+1][1]
        mid = (ev+od)//2

        if (ev+od) % 2 == 0:
            for j in range(ev-1):
                ans.append(0)

            ans.append(mid)
            ans.append(mid)

            for j in range(od-1):
                ans.append(0)
        else:
            if od % 2 == 1:
                for j in range(ev-1):
                    ans.append(0)

                ans.append(mid)
                ans.append(mid+1)

                for j in range(od-1):
                    ans.append(0)

            else:
                for j in range(ev-1):
                    ans.append(0)

                ans.append(mid+1)
                ans.append(mid)

                for j in range(od-1):
                    ans.append(0)





    print(*ans)


if __name__ == "__main__":
  main()
