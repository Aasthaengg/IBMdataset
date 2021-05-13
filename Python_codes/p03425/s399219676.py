N = int(input())

dic = {"M" : 0, "A": 0, "R": 0, "C": 0, "H": 0}
for _ in range(N):
  s = input()
  if s[0] in dic:
    dic[s[0]] += 1
      
char = ["M", "A", "R", "C", "H"]
ans = 0
for i in range(5):
  for j in range(i+1,5):
    for k in range(j+1,5):
      ans += dic[char[i]] * dic[char[j]] * dic[char[k]]
      
print(ans)