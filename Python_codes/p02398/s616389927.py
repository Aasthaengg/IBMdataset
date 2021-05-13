Input = input().split()
a = int(Input[0])
b = int(Input[1])
c = int(Input[2])
yakusuu = 0
if a >= 1 and b >= 1 and c >= 1:
    if a <= 10000 and b <= 10000 and c <= 10000:
        if a <= b:
            while a <= b:
                if c % a == 0:
                    yakusuu += 1
                a += 1
print(yakusuu)