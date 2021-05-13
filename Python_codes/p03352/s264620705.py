import sys
X = int(input())

if not ( 1 <= X <= 1000 ):
    sys.exit()

result = 1
for I in range(1,32):
    for J in range(2,10):
        if I ** J <= X and result <= I ** J:
            result = I ** J

print(result)