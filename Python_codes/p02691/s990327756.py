from collections import Counter

n=int(input())
A=list(map(int,input().split()) )

left = [i+A[i] for i in range(n)]
right = [i-A[i] for i in range(n)]

r_counter = Counter(right)

ans = 0

for l in left:
    ans += r_counter[l]

print(ans)