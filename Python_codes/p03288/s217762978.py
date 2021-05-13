r = int(input())
rate = 'AGC'

if r < 1200:
    rate='ABC'
elif r < 2800:
    rate='ARC'
print(rate)