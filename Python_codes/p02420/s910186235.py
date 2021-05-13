res = []

while True :
    Str = input()

    if Str == '-' : break

    res.append(Str)

    for mak in range(int(input()))  :
        shu = int(input())
        res[len(res)-1] = res[len(res)-1][shu:] + res[len(res)-1][:shu]

for mak in res : print(mak)