n = int(input())
a = list(map(int, input().split()))

odd = [a[i] for i in range(n) if i % 2 == 0]
even = [a[i] for i in range(n) if i % 2 == 1]

if n % 2 == 1:
   b = odd[::-1]
   b.extend(even)
else:
   b = even[::-1]
   b.extend(odd)
print(*b)
