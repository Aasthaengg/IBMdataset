k,s = map(int, input().split(" "))
count = 0
for i in range(max(0, s-2*k), min(s, k)+1):
  count += min(k, s-i) - max(0, s-i-k) + 1
  #print(count)
print(count)