x = int(input())
for i in range(8):
    if 400+200*i <= x <= 400+200*i+199:
        print(8-i)
        break