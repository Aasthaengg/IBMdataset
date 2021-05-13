ln = int(input())
word = input()
if ln >= len(word):
    print(word)
else:
    print(word[:ln],end=(''))
    print("...")