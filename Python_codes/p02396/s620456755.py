# encoding:utf-8
count = 1
while True:
    x = input()
    if '0' == x:
        break
    print("Case {0}: {1}".format(count, x)) 
    count += 1