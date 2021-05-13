import sys
input = sys.stdin.readline

n = int(input())
s = ["a"]
ord_a = ord("a")
ans = []

def dfs(s):
    if len(s) == n:
        ans.append("".join(s))
        return   
    max_ord = 0
    for i in s:
        max_ord = max(max_ord, ord(i) - ord_a)
    for j in range(max_ord + 2):
        new_s = s[:]
        new_s.append(chr(j + ord_a))
        dfs(new_s)
if n == 1:
    print("a")
    sys.exit()
dfs(s)
ans.sort()
for i in ans:
    print(i)
    





