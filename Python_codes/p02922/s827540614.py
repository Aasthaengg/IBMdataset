a, b = map(int, input().split())
taps=0
for i in range(40):
    taps = a*i-(i-1)
    if b <=  taps:
        break
print(i)