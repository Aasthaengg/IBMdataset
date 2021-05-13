import sys
s = input()
O = "keyence"
k = 0
for i in range(7,0,-1):
    if s[:i] == O[:i]:
        k = i
        if k == 7:
            print("YES")
            sys.exit()
        break
if s[len(s)+k-7:len(s)] == O[k:]:
    print("YES")
else:
    print("NO")
