n = int(input())
a = list(map(int, input().split()))
sa = set(a)
print("YES") if len(a) == len(sa) else print("NO")
