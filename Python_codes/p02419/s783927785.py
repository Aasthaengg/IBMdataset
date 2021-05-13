def count_if(f, lst):
    count = 0

    for l in lst:
        count += 1 if f(l) else 0

    return count

def main():
    count = 0

    word = input().lower()

    while True:
        line = input();

        if line == 'END_OF_TEXT':
            break

        count += count_if(lambda w: word == w.lower(), line.split())

    print(count)

if __name__ == '__main__':
    main()
