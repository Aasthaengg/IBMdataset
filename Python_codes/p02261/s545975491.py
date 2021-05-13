class Card():

    def bubble_sort(self):
        bubble_card = [i for i in self]
        for i in range(len(bubble_card)):
            for j in range(len(self)-1, i, -1):
                if bubble_card[j].strip('SHCD') < bubble_card[j-1].strip('SHCD'):
                    bubble_card[j], bubble_card[j-1] = bubble_card[j-1], bubble_card[j]
        return bubble_card


    def selection_sort(self):
        select_card = [i for i in self]
        for i in range(len(select_card)):
            minj = i
            change = False
            for j in range(i + 1, len(select_card)):
                if select_card[minj].strip('SHCD') > select_card[j].strip('SHCD'):
                    minj = j
                    change = True
            if change:
                select_card[i], select_card[minj] = select_card[minj], select_card[i]
        return select_card


    def stable_sort(self):
        sort_card = [i for i in self]
        sort = []
        for i in range(len(sort_card)-1):
            min = i
            for j in range(i+1, len(sort_card)):
                if int(sort_card[min].strip('SHCD')) > int(sort_card[j].strip('SHCD')):
                    min = j
            min_card = sort_card[min]
            sort_card.pop(min)
            sort_card.insert(i,min_card)
        sort = sort_card
        return sort





def main():
    n = int(input())
    cards = [i for i in input().split()]
    bubble = Card.bubble_sort(cards)
    select = Card.selection_sort(cards)
    stable = Card.stable_sort(cards)

    for i in range(len(bubble)):
        print(bubble[i]) if i == len(bubble)-1 else print(str(bubble[i])+' ',end='')
    print('Stable') if bubble == stable else print('Not stable')

    for i in range(len(select)):
        print(select[i]) if i == len(select)-1 else print(str(select[i])+' ',end='')
    print('Stable') if select == stable else print('Not stable')


if __name__ == '__main__':
    main()