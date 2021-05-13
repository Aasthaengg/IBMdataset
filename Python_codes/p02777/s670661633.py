s=input().split(" ")
a,b = map(int, input().split())
u = input()
ans = "Yes"

# print((a-1,b) if (s[0]==u) else a,b-1)
if s[0]==u:
    print(a-1,b)
else:
    print(a,b-1)