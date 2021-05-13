s =list(str(input()))
s_replace = [1 if i == "B" else 0 for i in s]
 
count = 0
ans = 0
 
for i in range(len(s_replace)):
  if s_replace[i] == 1: #もし黒だったらカウントしてください
    count += 1
    continue
  else: #もし白だったら黒の数を足してください
    ans = ans + count
    continue
    
print(ans)