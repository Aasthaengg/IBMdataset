O = list(input())
E = list(input())+[""]
o = len(O)
x =[]
for i in range(o):
  ans = O[i] + E[i]
  x.append(ans)

print("".join(x))