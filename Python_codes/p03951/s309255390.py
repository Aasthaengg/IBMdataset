n = int(input())
s = input()
t = input()
answer = n
for i in range (n + 1) :
  newstring = s[0:i] + t[:n]
  if newstring[0:n] == s:
    answer += i
    break
print (answer)