n = int(input())
a_list = list(map(int,input().split()))
s = 0
for a in a_list:
  s += a-1
print(s)