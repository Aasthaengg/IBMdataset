s, t = input().split()
a, b = map(int, input().split())
u = input()

if u==s:
    print(f"{a-1} {b}")
else:
    print(f"{a} {b-1}")