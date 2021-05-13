s = input()
answer  = 0
current = 0
for ch in s:
    if ch == "R":
        current += 1
    else:
        current = 0
    answer = max(answer, current)
 
print(answer)