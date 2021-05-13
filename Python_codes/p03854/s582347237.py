s = input()[::-1]

words = ["eraser","erase","dreamer","dream"]
for i in words:
  s = s.replace(i[::-1], "")
if s == "": print("YES")
else: print("NO")