N = int(input())
S = [True if i=='Y' else False for i in input().split()]
print('Four' if any(S) else 'Three')