def main():
    n = int(input())

    answers = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
    for _ in range(n):
        result = input()
        answers[result] += 1
    for key, value in answers.items():
        print(f'{key} x {value}')


if __name__ == '__main__':
    main()
