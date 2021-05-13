from math import sqrt

def standard_deviate(numbers):
    m = sum(numbers) / len(numbers)
    d = sqrt(sum([(n - m)**2 for n in numbers]) / len(numbers))
    return d

if __name__ == '__main__':
    while input() != '0':
        students = list(map(int, input().split()))
        print(standard_deviate(students))

