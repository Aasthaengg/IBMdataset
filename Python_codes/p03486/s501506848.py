s=list(input())
t=list(input())
s.sort()
t.sort(reverse=True)
diff=len(s)-len(t)
x= t if diff > 0 else s
x+=[" "]*abs(diff)

for i in range(len(s)):
  if s<t:
    print("Yes")
    exit()

print("No")
