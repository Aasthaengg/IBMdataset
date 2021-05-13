import sys
input = sys.stdin.readline

n = int(input())
s = input()

a = 0

for i in range(n-2):
    if s[i:i+3] == "ABC":
        a += 1

print(a)