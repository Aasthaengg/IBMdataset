n = int(input())
s = input()
t = input()

lst = []
for i in range(1,n+1):
    if s[n-i:] == t[:i]:
       lst.append(i+(n-i)*2)

if lst:
    print(min(lst))
else:
    print(n*2)

