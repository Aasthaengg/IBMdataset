while True:
    h, w = map(int, input().strip().split())
    if h == w == 0:
        break
    elif h > 2 and w > 2:
        print('#'*w+'\n'+('#'+'.'*(w-2)+'#\n')*(h-2)+'#'*w+'\n')
    else:
        print(('#' * w + '\n') * h)