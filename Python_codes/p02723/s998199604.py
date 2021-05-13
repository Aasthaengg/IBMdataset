ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

s=input()

if s[2]==s[3] and s[4]==s[5]:
  print('Yes')
  exit()
print("No")