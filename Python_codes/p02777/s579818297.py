first = input().split(" ")
second = input().split(" ")
third = input()

if third == first[0]:
    print(int(second[0])-1, second[1])
else:
    print(second[0], int(second[1])-1)