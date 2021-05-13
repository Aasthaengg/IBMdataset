n,k,q = map(int, input().split())
ac = [0] * n
for _ in range(q):
    a = int(input())
    ac[a-1] += 1

ss = sum(ac)
for a in ac:
    print('Yes' if k-ss+a > 0 else 'No')
