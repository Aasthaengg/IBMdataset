import bisect
import sys
sys.setrecursionlimit(10**9)

def main():
    N = int(input())
    S = list(input())

    a_ord = ord('a')
    z_ord = ord('z')

    set_list = [[] for _ in range(z_ord+1)]
    for i in range(N):
        s = S[i]
        set_list[ord(s)].append(i)

    Q = int(input())
    for q in range(Q):
        ipt = input().split()
        if ipt[0] == "1":
            i,c = int(ipt[1]), ipt[2]
            j = ord(S[i-1])

            if j == ord(c): continue
            set_list[j].remove(i-1)
            bisect.insort_left(set_list[ord(c)],i-1)
            S[i-1] = c
            # print(set_list[])

        else:
            l,r = int(ipt[1]), int(ipt[2])
            ans = 0
            # if l == r:
            #     print(1)
            #     continue

            for i in range(a_ord,z_ord+1):
                st = set_list[i]
                if not len(st) > 0: continue

                # print(i,set_list[i])
                l_p = bisect.bisect_left(st,l-1)
                r_p = bisect.bisect_right(st,r-1)

                # print(l-1,r-1,l_p,r_p)
                if l_p < r_p:
                    ans += 1

            # print(ans,"____")
            print(ans)



if __name__ == "__main__":
  main()
