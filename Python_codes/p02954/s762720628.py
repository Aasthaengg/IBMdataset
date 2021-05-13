s = input()

buf = [1]*len(s) # 各マスに一人いる状態

for i in range(len(buf)-2): 
  # RとLが隣り合っている場合は最終的に移動することは無いので、連続している場合のみを対象として移動を行う。
  if s[i] == "R" and s[i+1] == "R": 
    buf[i+2] += buf[i]
    buf[i] = 0
    
for i in range(len(buf)-1, 1, -1):
  if s[i] == "L" and s[i-1] == "L":
    buf[i-2] += buf[i]
    buf[i] = 0
    
print(" ".join(map(str, buf)))