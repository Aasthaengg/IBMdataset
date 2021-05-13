from sys import stdin
s = (stdin.readline().rstrip())
s = s.replace("BC","D")
ans = 0
acc = 0

for i in s:
    if i == "B" or i == "C":
        acc = 0
        continue
        
    if i == "A":
        acc += 1
    
    if i == "D":
        ans += acc

print(ans)