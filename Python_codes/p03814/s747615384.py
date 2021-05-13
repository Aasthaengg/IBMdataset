s = list(input())
start = 0
end = 0
len_s = len(s)
for i in range(len_s):
  if s[i] == "A":
    start = i
    break
    
for i in reversed(range(len_s)):
  if s[i] == "Z":
    end = i
    break
print(end - start + 1)