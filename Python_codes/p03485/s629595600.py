a, b = map(int, raw_input() .split())
if (a + b) % 2 == 0:
    print (a + b)/2
elif a + b % 2 != 0:
    print (a + b)/2 + 1
