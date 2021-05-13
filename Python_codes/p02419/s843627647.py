W = input().lower()
T = []
while True:
    S = input()
    if S == "END_OF_TEXT":
        break
    T.extend([words.lower() for words in S.split()])
print(T.count(W))