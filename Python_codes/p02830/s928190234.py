lt = int(input())

s,t = map(str, input().split())
string = ""
for i in range(0, lt):
  string = string + s[i] + t[i]
  
print(string)