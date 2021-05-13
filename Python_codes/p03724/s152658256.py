def main():
    n, m = map(int, input().split())
    ab = [sorted(list(map(int, input().split()))) for _ in [0] * m]
    l = [0] * (n - 1)
    for i in range(m):
        a, b = ab[i]
        if a != 1:
            l[a-2]+=1
        l[b - 2] += 1
    l=[i%2 for i in l]
    if sum(l) > 0:
        print("NO")
    else:
        print("YES")
main()