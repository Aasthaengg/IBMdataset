n = int(input())
s = 0
for i in input().split(' '):
 s += int(i)
print("YES" if s%2 == 0 else "NO")