def grade(half, end, reexam):
    points = half + end
    if half == -1 or end == -1:
        return 'F'
    else:    
        if points >= 80:
            return 'A'
        elif points >= 65:
            return 'B'
        elif points >= 50:
            return 'C'
        elif points >= 30:
            if reexam >= 50:
                return 'C'
            else:
                return 'D'
        else:
            return 'F'

while 1:
    half, end, reexam = map(int, input().split())
    if half == end == reexam == -1:
        break
    else:
        print(grade(half, end, reexam))
