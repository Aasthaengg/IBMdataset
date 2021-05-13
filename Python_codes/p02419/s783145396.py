import sys
W = input()
ans = 0
while True:
    T = list(map(str,input().split()))
    if T[0] == "END_OF_TEXT":break
    for i in T:
        if W == i.lower():ans += 1
print(ans)
