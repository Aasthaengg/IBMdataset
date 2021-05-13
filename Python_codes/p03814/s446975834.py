import sys
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

s = LS2()
a = 0
for i in range(len(s)):
    if s[i] == 'A':
        a = i
        break
b = 0
for i in range(len(s)-1,-1,-1):
    if s[i] == 'Z':
        b = i
        break
print(b-a+1)