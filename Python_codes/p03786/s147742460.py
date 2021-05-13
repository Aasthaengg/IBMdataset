N = int(input())
A = sorted(map(int,input().split()))


last_impossible = 0
s = 0
for i,a in enumerate(A):
    if a > 2*s:
        last_impossible = i
    s += a

print(N-last_impossible)
