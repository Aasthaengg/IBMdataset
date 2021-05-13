while True:
    h, w = map( int, input().split() )
    if not h and not w:
        break
    if h <3 or w < 3:
        print(("#" * w + "\n") * h)
    else:
        print('#' * w +'\n' + ('#' + '.' * (w-2) + '#\n') * (h-2) + '#' * w + '\n')