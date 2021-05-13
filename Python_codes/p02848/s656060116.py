def rot_n():
    n = int(input())
    s = input()

    answer = ''
    for letter in s:
        answer += chr(ord('A') + (ord(letter)-ord('A')+n) % 26)

    print(answer)


if __name__ == '__main__':
    rot_n()