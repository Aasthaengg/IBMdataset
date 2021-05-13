# -*-coding:utf-8

def main():

    while True:
        deck = input()
        if(deck == '-'):
            break

        shuffleTime = int(input())

        for i in range(shuffleTime):
            rollNumber = int(input())
            deck = deck[rollNumber:] + deck[:rollNumber]

        print(''.join(deck))


if __name__ == '__main__':
    main()