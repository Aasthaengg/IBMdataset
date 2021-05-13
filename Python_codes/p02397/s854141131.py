flag = 1
while flag:
    numbers = []
    n = raw_input()
    numbers = n.split(" ")
    x = int(numbers[0])
    y = int(numbers[1])
    if x == 0 and y == 0:
    	flag = 0
    	continue
    if x >= y:
    	x, y = y, x
    print x, y