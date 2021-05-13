n = int(input())
s = input()

for i in range(1,n):
    s_1 = set(s[:i])
    s_2 = set(s[i:])
    lis = [len(set(s[:i])&set(s[i:])) for i in range(1,n) ]
print(max(lis))