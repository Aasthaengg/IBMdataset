n = int(input())
s = input().split()
ss = list(set(s))
print('Four' if len(ss)==4 else 'Three')