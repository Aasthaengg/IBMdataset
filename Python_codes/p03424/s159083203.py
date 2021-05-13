
n = int(input())
s = list(input().split())
s_set = set(s)
print("Four" if len(s_set) == 4 else "Three")
