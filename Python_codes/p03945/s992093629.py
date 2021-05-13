import re
string = input()
ans = 0
for i in range(len(string)-1):
    if string[i] != string[i+1]:
        ans += 1
print(ans)