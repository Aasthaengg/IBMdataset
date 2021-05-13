input1 = raw_input()

split_input = input1.split()

if(split_input[1] == u'+'):
    print int(split_input[0]) + int(split_input[2])
else:
    print int(split_input[0]) - int(split_input[2])