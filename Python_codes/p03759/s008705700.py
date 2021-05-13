a,b,c = map(int, input().split())
print('YNEOS'[not((b-a)==(c-b))::2])