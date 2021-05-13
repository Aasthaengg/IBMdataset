answers=[]
while True:
    cards=input()
    if cards=='-':
        break
    shuffle=int(input())
    for i in range(shuffle):
        num_of_cards=int(input())
        cards=cards[num_of_cards::]+cards[:num_of_cards:]
    answers.append(cards)

for i in answers:
    print(i)