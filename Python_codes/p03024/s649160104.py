import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

lst1 = ["o"]*15
s = readline().rstrip().decode('utf-8')
for i in range(len(s)):
    lst1[i] = s[i]

if lst1.count("o") >= 8:
    print("YES")
else:
    print("NO")