hoge = list()
for elem in (elem for elem in input().split()):
    if elem == '+':
        elem = int(hoge.pop()) + int(hoge.pop())
    elif elem == '*':
        elem = int(hoge.pop()) * int(hoge.pop())
    elif elem == '-':
        elem = -1*int(hoge.pop()) + int(hoge.pop())
    hoge.append(elem)
print (elem)
