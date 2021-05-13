a, b, k = map(int, input().split())

s1 = [i for i in range(a, a+k) if i<=b]
s2 = [i for i in range(b-k+1, b+1) if i>=a]

s = list(set(s1+s2))
s.sort()

for i in s:
    print(i)