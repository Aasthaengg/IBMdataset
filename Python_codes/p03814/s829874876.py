s = input()
end = 0
for i in range(len(s) - 1, -1, -1):
  if s[i] == 'Z':
    end = i + 1
    break
    
print(len(s[s.index('A'):end]))