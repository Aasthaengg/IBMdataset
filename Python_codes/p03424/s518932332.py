n = int(input())
lists = input().split()

sets = set(lists)
if len(sets) == 3:
    ans = 'Three'
else:
    ans = 'Four'

print(ans)