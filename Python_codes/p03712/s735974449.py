h, w = map(int, input().split())
s = [list(input()) for i in range(h)]
s = [["#"] + i + ["#"] for i in s]
s = [["#" for i in range(w+2)]] + s + [["#" for i in range(w+2)]]
for i in range(h+2):
  print("".join(s[i]))