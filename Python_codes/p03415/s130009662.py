c1 = [""] * 3
c2 = [""] * 3
c3 = [""] * 3
for i in range(3):
  c1[i],c2[i],c3[i] = list(str(input()))
ans = ""
ans += c1[0]
ans += c2[1]
ans += c3[2]
print(ans)