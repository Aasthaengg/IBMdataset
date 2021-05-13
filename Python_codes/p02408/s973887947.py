num = int(input())

cards = list()

for i in range(num):
    cards.append(input())

pics = ['S', 'H', 'C', 'D']
nums = [str(i) for i in range(1, 14)]

for p in pics:
    for n in nums:
        c = p+' '+n
        if not c in cards:
            print(c)