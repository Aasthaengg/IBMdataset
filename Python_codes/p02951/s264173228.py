A, B, C = map(int,input().split())

if A >= (B + C):
    answer = 0
else:
    answer = (B + C) - A
print(answer)