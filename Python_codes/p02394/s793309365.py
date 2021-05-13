def circle_in_rectangle(radius, pos, height, width):
    """
    radius: int
    pos: tuple, (x, y)
    height: int, height of rectangle
    width: int, width of rectangle

    returns True if circle is in rectangle, otherwise False

    >>> circle_in_rectangle(1, (1, 1), 4, 5)
    True
    >>> circle_in_rectangle(1, (2, 4), 4, 5)
    False
    """
    (x, y) = pos
    if x < radius or x > width - radius:
        return False

    if y < radius or y > height - radius:
        return False

    return True

if __name__ == '__main__':
    #import doctest
    #doctest.testmod()

    (w, h, x, y, r) = input().split(' ')

    if circle_in_rectangle(int(r), (int(x), int(y)), int(h), int(w)):
        print('Yes')
    else:
        print('No')