#coding:utf-8
#1_1_A
def insertion_sort(cards, n):
    for i in range(n):
        v = cards[i]
        j = i - 1
        while j >= 0 and cards[j] > v:
            cards[j+1] = cards[j]
            j -= 1
        cards[j+1] = v
        print(*cards)

n = int(input())
cards = list(map(int, input().split()))
insertion_sort(cards, n)