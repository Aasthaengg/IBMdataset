s = input()
abc = [s.count("a"),s.count("b"),s.count("c")]
if max(abc)-min(abc)<=1:
  print("YES")
else:
  print("NO")