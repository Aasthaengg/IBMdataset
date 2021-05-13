args=input()
list= args.split()
list_i = [int(s) for s in list]
if list_i[0] * list_i[1] % 2 == 1:
    print('Odd')
else:
    print('Even')