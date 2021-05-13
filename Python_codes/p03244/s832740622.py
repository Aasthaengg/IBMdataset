from collections import defaultdict

def main():
    n = int(input())
    vlst = list(map(int, input().split()))
    dd = [defaultdict(int), defaultdict(int)]
    dd[0][-1] = 0
    dd[1][-1] = 0
    for i, v in enumerate(vlst):
        dd[i % 2][v] += 1
    odd = sorted(dd[0].items(), key = lambda x:x[1], reverse = True)
    even = sorted(dd[1].items(), key = lambda x:x[1], reverse = True)
    if odd[0][0] != even[0][0]:
        minus = odd[0][1] + even[0][1]
        ans = n - minus
    else:
        minus = 0
        minus = max(minus, odd[0][1] + even[1][1])
        minus = max(minus, odd[1][1] + even[0][1])
        ans = n - minus
    print(ans)
main()