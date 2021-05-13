N = int(input())
number = []
for i in range(N):
    number.append(int(input()))
sorted_number = sorted(number,reverse=True)
max_number = sorted_number[0]
second_number = sorted_number[1]

for i in number:
    if i != max_number:
        print(max_number)
    else:
        print(second_number)
