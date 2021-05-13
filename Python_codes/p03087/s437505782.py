import sys
input = sys.stdin.readline
n, q = [int(w) for w in input().split()]

s = input()
c_ac = [0]*(len(s)+1)

is_p_c = False
for i in range(len(s)-1, -1, -1):
    if s[i] == "A"and is_p_c:
        c_ac[i] = c_ac[i+1]+1
    else:
        c_ac[i] = c_ac[i+1]
    if s[i] == "C":
        is_p_c = True
    else:
        is_p_c = False


for i in range(q):
    l, r = [int(w)-1 for w in input().split()]
    print(c_ac[l]-c_ac[r])
