# -*- coding: utf-8 -*-

def main():

    C = input()

    alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    listAlphabet = alphabet.split()

    for i, name in enumerate(listAlphabet):
        if name == C:
            ans = listAlphabet[i + 1]
            break

    print(ans)


if __name__ == "__main__":
    main()