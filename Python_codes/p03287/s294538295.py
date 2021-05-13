from collections import Counter
def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = [0]
    for a in A:
        B.append((B[-1]+a)%M)
    c = Counter(B)
    ans = 0
    for v in c.values():
        ans += v*(v-1)//2
    print(ans)

if __name__ == '__main__':
    main()