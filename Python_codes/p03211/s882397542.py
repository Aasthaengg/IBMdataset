s=list(input())
diff=1000000
for i in range(len(s)-2):
  x=int(''.join(s[i:i+3]))
  diff = min(diff, abs(753-x))
  #print(x)
print(diff)