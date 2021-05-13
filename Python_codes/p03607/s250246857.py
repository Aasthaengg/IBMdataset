#-*-coding:utf-8-*-

from collections import Counter

def main():
    n = int(input())
    numbers=[]
    answers=[]
    number=0
    numbers=[int(input()) for _ in range(n)]
    Numbers_col = Counter(numbers)

    for number in Numbers_col.values():
        if number%2!=0:
            answers.append(number)
    print(len(answers))

if __name__=="__main__":
    main()