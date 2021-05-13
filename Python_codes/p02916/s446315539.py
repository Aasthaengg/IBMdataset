n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

sat = 0
ai_prev = None
for ai in a:
    sat += b[ai - 1]
    if ai_prev == ai - 1:
        sat += c[ai_prev - 1]
    ai_prev = ai
print(sat)
