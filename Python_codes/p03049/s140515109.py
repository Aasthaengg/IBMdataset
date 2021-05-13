import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
B_A = 0
start_B = 0
end_A = 0
ans = 0
for _ in range(N):
    s = input()
    ans += s.count('AB')
    if s[0]=='B' and s[-1]=='A':
        B_A += 1
    elif s[0]=='B':
        start_B += 1
    elif s[-1]=='A':
        end_A += 1

if B_A>=1:
    ans += B_A - 1
    B_A = 1
ans += min(B_A, start_B) + min(B_A, end_A) + max(min(start_B - B_A, end_A - B_A), 0)
print(ans)