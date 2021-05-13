n,k = map(int,input().split())
s = list(input())
change = 0
for i in range(n-1):
  if s[i] != s[i+1]:
    change += 1
happy = n-change-1
print(min(n-1,happy+min(k,change)*2))