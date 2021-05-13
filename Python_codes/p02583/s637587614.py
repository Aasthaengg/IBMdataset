n = int(input())
a = [int(x) for x in input().split()]

result = 0

for a_i in range(n):
  for b_i in range(a_i+1, n):
    for c_i in range(b_i+1, n):
      l_a = a[a_i]
      l_b = a[b_i]
      l_c = a[c_i]
      
      if l_a == l_b or l_b == l_c or l_a == l_c:
        continue

      if l_a + l_b > l_c and l_b + l_c > l_a and l_c + l_a > l_b:
        result += 1
print(result)