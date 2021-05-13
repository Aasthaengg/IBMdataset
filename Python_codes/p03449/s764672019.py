n = int(input())
la1 = [int(w) for w in input().split()]
la2 = [int(w) for w in input().split()]


ans = 0
for i in range(n):
    s1 = sum(la1[:i + 1])
    s2 = sum(la2[i:])
    ans = max(ans, s1 + s2)
print(ans)
