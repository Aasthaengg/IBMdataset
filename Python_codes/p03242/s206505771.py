n = list(input())

print(int(''.join(['1' if i=='9' else '9' for i in n])))