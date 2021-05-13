while True:
    ls = raw_input()
    if ls == '-': break
 
    m = int(raw_input())
    for i in range(m):
        h = int(raw_input())
        ls = ls[h:] + ls[:h]
    print ls
