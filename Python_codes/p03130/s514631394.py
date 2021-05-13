def cin():  return list(map(int,input().split()))
c = [0] * 4
for i in range(3):
    in1, in2 = cin()
    c[in1 - 1] += 1
    c[in2 - 1] += 1
c = sorted(c)
if c == [1, 1, 2, 2]:  print("YES")
else:  print("NO")