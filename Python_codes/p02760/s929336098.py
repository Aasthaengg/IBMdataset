A = []
for i in range(3):
    A.extend(input().split())
N = int(input())
b = []
for i in range(N):
    b.append(input())

card = [False] * 9
for selection in b:
    for i, a in enumerate(A):
        if selection == a:
            card[i] = True

# judge
answer = 'No'
# row
if (card[0] and card[1] and card[2]) \
or (card[3] and card[4] and card[5]) \
or (card[6] and card[7] and card[8]):
    answer = 'Yes'
# col
if (card[0] and card[3] and card[6]) \
or (card[1] and card[4] and card[7]) \
or (card[2] and card[5] and card[8]):
    answer = 'Yes'
# cross
if (card[0] and card[4] and card[8]) \
or (card[2] and card[4] and card[6]):
    answer = 'Yes'
print(answer)
