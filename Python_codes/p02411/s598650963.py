# coding=utf-8

def main():
    while True:
        line = raw_input()
        if line == '-1 -1 -1':
            break
        middle, final, re = map(int, line.split())
        if middle == -1 or final == -1:
            grade = 'F'
        elif middle + final >= 80:
            grade = 'A'
        elif 65 <= middle + final < 80:
            grade = 'B'
        elif 50 <= middle + final < 65:
            grade = 'C'
        elif 30 <= middle + final < 50:
            if 50 <= re:
                grade = 'C'
            else:
                grade = 'D'
        elif middle + final < 30:
            grade = 'F'
        print grade

if __name__ == '__main__':
    main()