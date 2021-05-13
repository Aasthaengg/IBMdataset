n = int(input())
s = input().split()
s = set(s)
print('Four' if len(s) == 4 else 'Three')