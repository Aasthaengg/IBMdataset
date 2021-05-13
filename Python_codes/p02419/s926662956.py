cnt = 0

W = input()

while True:
    T = input().split()
    if T[0] == "END_OF_TEXT":
        break
    for word in T:
        if W.lower() == word.lower():
            cnt += 1

print(cnt)