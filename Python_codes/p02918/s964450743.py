n,k = map(int, input().split())
s = input()
happy, no = 0,0
for i in range(1,n):
    if s[i] == s[i-1]:
        happy += 1
    else: no += 1

for i in range(k):
    if no == 1:
        no -= 1
        happy += 1
        break
    no -= 2
    happy += 2
print(min(happy, n-1))