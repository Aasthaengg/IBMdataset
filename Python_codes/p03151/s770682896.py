from bisect import bisect_left

def main():
    N = int(input())
    A = tuple(map(int, input().split()))
    B = tuple(map(int, input().split()))

    surplus = []
    need = 0
    ans = 0
    for a, b in zip(A, B):
        diff = a - b
        if diff > 0:
            surplus.append(diff)
        if diff < 0:
            need += -diff
            ans += 1

    surplus.sort(reverse=True)
    cusum = [0] * (len(surplus) + 1)
    for i, sur in enumerate(surplus):
        cusum[i+1] = cusum[i] + sur

    plus = bisect_left(cusum, need)
    ans += plus
    if need and plus == len(cusum):
        print(-1)
    else:
        print(ans)
    
if __name__ == "__main__":
    main()