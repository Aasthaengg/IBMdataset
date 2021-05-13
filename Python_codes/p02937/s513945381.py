import bisect
import sys
sys.setrecursionlimit(10**9)

def main():
    S, T = list(input()),list(input())

    len_of_S = len(S)
    counter = {}
    seen = set()
    for i in range(len_of_S):
        if S[i] in seen:
            counter[S[i]].append(i) # 常に単調増加
        else:
            counter[S[i]] = [i]
            seen.add(S[i])

    len_of_T = len(T)

    if not T[0] in seen:
        print(-1)
        exit()

    counts = counter[T[0]]
    if len(counts) == 0:
        print(-1)
        exit()

    pre = counts[0]
    rep = 1

    for i in range(1,len_of_T):
        if not T[i] in seen:
            print(-1)
            exit()

        counts = counter[T[i]]
        if len(counts) == 0:
            print(-1)
            exit()

        j = bisect.bisect_left(counts,pre)
        mx = len(counts)

        while j < mx and not counts[j] > pre:
            j += 1

        # print(pre,rep)
        if j<mx:
            pre = counts[j]
        else:
            pre = counts[0]
            rep += 1
        # print(pre,rep)

    # print(counter[T[::-1][0]],len_of_S)
    rep -= 1
    ans = rep * len_of_S  + pre + 1
    print(ans)




if __name__ == "__main__":
  main()