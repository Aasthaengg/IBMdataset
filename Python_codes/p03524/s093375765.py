s = input()
cnt = [s.count("a"),s.count("b"), s.count("c")]
if sum(cnt) == 1: print("YES")
elif len(set(s)) == 1 or max(cnt) - min(cnt) > 1: print("NO")
else: print("YES")