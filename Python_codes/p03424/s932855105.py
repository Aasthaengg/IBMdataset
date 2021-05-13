n = int(input())
s = input().split()
print('Four' if len(set(s)) == 4 else 'Three')